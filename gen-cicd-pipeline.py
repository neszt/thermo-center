#!/usr/bin/env python

import copy
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

droneTemplateFile = ".drone.build.yml"
droneManifestTemplateFile = ".drone.manifest.yml"
droneFile = ".drone.yml"
manifestsBase = "manifests"
architectures = ("arm","amd64")

def parseYaml(f: str):
    with open(f, "r") as fh:
        return yaml.load(stream=fh, Loader=Loader)


def gen_manifest_tmpl(repo: str):
    filename = repo.replace('/', '-')
    path = '{}/{}.tmpl'.format(manifestsBase, filename)
    with open(path, 'w') as mf:
        mf.write("""image: @REPO@:{{#if build.tag}}{{trimPrefix "v" build.tag}}{{else}}latest{{/if}}
{{#if build.tags}}
tags:
{{#each build.tags}}
- {{this}}
{{/each}}
{{/if}}
manifests:
""".replace('@REPO@', repo))

        for arch in architectures:
            mf.write("""- image: @REPO@:{{#if build.tag}}{{trimPrefix "v" build.tag}}-{{/if}}@ARCH@
  platform:
    architecture: @ARCH@
    os: linux
""".replace('@REPO@', repo).replace('@ARCH@', arch))

    return path


if __name__ == "__main__":
    pipelines = []
    repos = []

    bt = parseYaml(droneTemplateFile)
    for step in bt['steps']:
        if step['image'] == 'plugins/docker':
            repos.append(step['settings']['repo'])

    mt = parseYaml(droneManifestTemplateFile)

    with open(droneFile, "w") as out:
        for arch in architectures:
            buildName = "build-{}".format(arch)
            pipelines.append(buildName)

            bt['name'] = buildName
            bt['platform']['arch'] = arch

            for step in bt['steps']:
                if step['image'] == 'plugins/docker':
                    step['settings']['auto_tag_suffix'] = arch

            out.write('---\n')
            out.write('### Autogenerated pipeline! DONT edit! ###\n')
            yaml.dump(bt, out, Dumper=Dumper)

        manifestStep = mt['steps'][0]
        mt['steps'] = []
        mt['depends_on'] = pipelines

        # Run manifest pipeline on first defined architecture
        mt['platform']['arch'] = architectures[0]

        for repo in repos:
            step = copy.deepcopy(manifestStep)
            step['name'] = repo
            manifestfile = gen_manifest_tmpl(repo)
            step['settings']['spec'] = manifestfile

            mt['steps'].append(step)

        out.write('---\n')
        yaml.dump(mt, out, Dumper=Dumper)

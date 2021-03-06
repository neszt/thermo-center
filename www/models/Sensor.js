'use strict';
import meta from './g/Sensor';
import DefineMap from 'can-define/map/map';
import DefineList from 'can-define/list/list';
import assign from 'can-assign';
import {tastypieRestModel} from '../tastypie';

const staticProps = {
    seal: true,
};
const prototype = {
};
assign(prototype, meta.d);

const Sensor = DefineMap.extend('Sensor', staticProps, prototype);
Sensor.List = DefineList.extend('SensorList', {'#': Sensor});

Sensor.connect = tastypieRestModel({
    Map: Sensor,
    List: Sensor.List,
    url: meta.e,
});

export {Sensor, Sensor as default};

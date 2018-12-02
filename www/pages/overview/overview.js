'use strict';
import {Component} from 'can';
import {THSensor} from 'models/THSensor';

Component.extend({
	tag: 'thermo-p-overview',
	view: `
		<table class="table table-striped table-bordered table-hover table-sm">
		<thead>
		<tr>
			<th>Name</th>
			<th>Temperature</th>
			<th>Humidity</th>
			{{#advanced}}
			<th>ID</th>
			<th>VCC</th>
			<th>Interval</th>
			<th>RSSI</th>
			<th>LQI</th>
			{{/advanced}}
			<th>Op</th>
		</tr>
		</thead>
		<tbody>
		{{#for(s of this.sensors)}}
			<tr class="">
				<td>{{s.name}}</td>
				<td>{{format('temperature', s.temperature)}}</td>
				<td>{{format('humidity', s.humidity)}}</td>
				{{#advanced}}
				<td>{{s.id}}</td>
				<td>{{format('vcc', s.vcc)}}</td>
				<td>{{format('interval', s.interval)}}</td>
				<td>{{format('rssi', s.rssi)}}</td>
				<td>{{format('lqi', s.lqi)}}</td>
				{{/advanced}}
				<td><sensor-resync sensor:bind="s" /></td>
			</tr>
		{{/for}}
		</tbody>
		</table>
		<div class="checkbox">
			<label>
				<input type="checkbox" checked:bind="advanced" />
				Show advanced fields
			</label>
		</div>
	`,
	ViewModel: {
		sensors: { default: () => [] },
		advanced: 'boolean',
		connectedCallback(element) {
			var self = this;
			THSensor.getList({'order_by': 'id'}).then(function(res) {
				self.sensors = res;
			});

			self.appstate.onmessage = function(el) {
				THSensor.get({id: el});
			};

			return function() {
				self.appstate.onmessage = null;
				self.stopListening();
			};
		}
	}
});

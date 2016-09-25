import THSensor from 'models/Thsensor';
import 'can/component/';
import list from './list.stache!';
import sensor from './sensor.stache!';

can.Component.extend({
	tag: 'overview-sensor',
	template: sensor,
	viewModel: {
		expand: false,
		classes() {
			if (this.sensor.getValid() === false) {
				return 'text-warning';
			}

			return '';
		},
		can_resync() {
			return this.sensor.attr('sensor_resync') != null;
		},
		do_resync() {
			this.sensor.getSensor_resync().then(function(o) {
				o.save();
			});
		},
		toggle() {
			this.attr('expand', !this.attr('expand'));
		}
	},
	helpers: {
		format_num(value, fix) {
			value = value();

			if (typeof(value) == 'number') {
				return value.toFixed(fix);
			}

			return value;
		}
	}
});

can.Component.extend({
	tag: 'page-overview',
	template: list,
	viewModel: {
		sensors: []
	},
	events: {
		inserted() {
			var view = this.viewModel;
			THSensor.findAll({'order_by': 'id'}).then(function(res) {
				view.attr('sensors', res);
				can.each(res, function(s) {
					s.startRefresh();
				});
			});
		},
		removed() {
			var view = this.viewModel;
			can.each(view.sensors, (s) => s.stopRefresh());
		}
	}
});

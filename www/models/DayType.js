'use strict';
import meta from './g/DayType';
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

const DayType = DefineMap.extend('DayType', staticProps, prototype);
DayType.List = DefineList.extend('DayTypeList', {'#': DayType});

DayType.connect = tastypieRestModel({
    Map: DayType,
    List: DayType.List,
    url: meta.e,
});

export {DayType, DayType as default};

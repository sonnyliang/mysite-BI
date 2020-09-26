import Vue from 'vue'
import App from './App.vue'
import store from './store' //引入状态管理 store

import Vcharts from 'v-charts'

import router from './router.js'

import Axios from 'axios'

import api from './api'

import Resource from 'vue-resource'

// 用于新建proxTable 解决跨域问题
// import Resource from 'vue-resource'

// 引入样式
import 'vue-easytable/libs/themes-base/index.css'
// 导入 table 和 分页组件
import {VTable,VPagination} from 'vue-easytable'
Vue.use(VTable)
Vue.use(VPagination)
// 注册到全局
Vue.component(VTable.name, VTable)
Vue.component(VPagination.name, VPagination)


Vue.use(Resource)

// vue-bootstrap-datetimepicker
import 'pc-bootstrap4-datetimepicker/build/css/bootstrap-datetimepicker.css'
import '@fortawesome/fontawesome-free/css/all.css'


// 使用BootstrapVue  -start
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
// 使用BootstrapVue  -end

// Vue.use(Vuex)

// vue-resource 在vue2.0后不再支持
// Vue.use(Resource)
// Vue.config.productionTip = false


Vue.use(Vcharts)

// 使用axios
Vue.prototype.$axios = Axios; //全局注册，使用方法为:this.$axios
Vue.prototype.HOST = '/api';
Vue.config.productionTip = false;


new Vue({
  router,
  store, //注册store(这可以把 store 的实例注入所有的子组件)
  api,
  render: h => h(App)
}).$mount('#app')

import axios from 'axios';
// import Qs from 'qs'; // 用来处理参数，可不使用，若要使用，npm安装： npm install qs
axios.defaults.baseURL = 'http://127.0.0.1:8000/'; // 请求的默认域名
// 添加一个请求拦截器
// axios.interceptors.request.use(config => {
//         config.headers.languagetype = 'CN'; // 举例，加上一个公共头部
//         config.data = Qs.stringify(config.data); // 处理数据，可不写
//         return config;
//     },
//     err => {
//         return Promise.reject(err);
//     });

// //添加一个响应拦截器
// axios.interceptors.response.use(res => {
//     //在这里对返回的数据进行处理
//     console.log(res.data, '网络正常');
//     return res.data;
// }, err => {
//     console.log('网络开了小差！请重试...');
//     return Promise.reject(err);
// });

export default axios 
<template>
    <div class='container-fluid'>
        <Display/> 
        <div class='row-fluid'>
            <h1>this is a test page</h1>
            <!-- 添加click事件函数 -->
            <button @click='vueResourceTest'>vueResourceTest</button>
            <button @click='axiosTest'>axiosTestTest</button>
        </div>
    </div>
</template>



<script>

import Display from '../components/Display.vue'
import axios from 'axios'

export default{
    name: 'BI',
    data(){
        return {}
    },
    // click事件的处理函数
    methods:{
        // 已启用vue-resource
        vueResourceTest:function(){
            this.$http.get('/bi/api/test').then(res => {
                console.log(res)
            })
        },
        axiosTest:function(){
            axios.get('/bi/api/test').then(response => {
                if (response.data) {
                    console.log(response.data)
                }
            }).catch(error => {alert(error)})
        },
    },
    components: {
        Display,
    },
}
</script>
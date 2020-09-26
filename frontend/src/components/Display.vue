<template>
    <div>
        <div id="nav">
            <!-- 动态组件 -->
            <button @click="currentComponent = 'BICharts'">图例</button>
            <button @click="currentComponent = 'keyIndex'">指标</button>
            <button @click="currentComponent = 'Table'">透视表</button>
            <!-- 动态组件：keep-alive 状态保持，避免切换组件后被初始化 -->
            <keep-alive>
              <component :is="currentComponent"/>
            </keep-alive>
        </div>
    </div>
</template>




<script>
import BICharts from './BICharts.vue'
import KeyIndex from './KeyIndex.vue'
import Table from './Table.vue'

export default{
  data(){
      return{
        currentComponent: 'BICharts'
      }
  },
  components: {
    BICharts,
    KeyIndex,
    Table,
  },
}
</script>
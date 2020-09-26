<template>
    <div class='row'>
        <div class='col-md-3'>
            <BIFilter @testValue="getSubValue"/>
        </div>
        <div class='col-md-9'>
            <v-table
                :width="100"
                :columns="columns"
                :table-data="tableData"
                :show-vertical-border="true"
                row-hover-color="#eee"
                row-click-color="#edf7ff"
            ></v-table>
            <button @click='getData'>getData</button>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import BIFilter from '../components/BIFilter.vue'
 
export default{
    data: function() {
        return {
            // tableData: [
            //     {"name":"赵伟","tel":"156*****1987","hobby":"钢琴、书法、唱歌","address":"上海市黄浦区金陵东路569号17楼"},
            //     {"name":"李伟","tel":"182*****1538","hobby":"钢琴、书法、唱歌","address":"上海市奉贤区南桥镇立新路12号2楼"},
            //     {"name":"孙伟","tel":"161*****0097","hobby":"钢琴、书法、唱歌","address":"上海市崇明县城桥镇八一路739号"},
            //     {"name":"周伟","tel":"197*****1123","hobby":"钢琴、书法、唱歌","address":"上海市青浦区青浦镇章浜路24号"},
            //     {"name":"吴伟","tel":"183*****6678","hobby":"钢琴、书法、唱歌","address":"上海市松江区乐都西路867-871号"}
            // ],
            // columns: [
            //     {field: 'name', title:'姓名', width: 100, titleAlign: 'center',columnAlign:'center'},
            //     {field: 'tel', title: '手机号码', width: 260, titleAlign: 'center',columnAlign:'center'},
            //     {field: 'hobby', title: '爱好', width: 330, titleAlign: 'center',columnAlign:'center'},
            //     {field: 'address', title: '地址', titleAlign: 'center',columnAlign:'left'}
            // ]
            tableData: [],
            columnField: [],
            columns: [],
        }
    },
    methods:{
        getData:function(){
            axios.get('/bi/api/paramtest/').then(res => {
                console.log(res.data);
                this.tableData=res.data;
            })
        },
        getSubValue:function(Value){
            this.tableData = Value;
            this.columnField = Object.keys(Value[0]);
            console.log('成功接收数据');
            this.columns=[];
            for(let i=0; i<this.columnField.length; i++){
                this.columns.push(
                    {'field':this.columnField[i],
                    'title':this.columnField[i],
                    'width': 100,
                    'titleAlign': 'center',
                    'columnAlign':'center',
                    'isResize':true}
                )
            }
        },
    },
    components: {
    BIFilter,
    },
}
</script>
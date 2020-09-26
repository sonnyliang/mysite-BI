<template>
<form>
    <div class="form-group">
        <label for="exampleSelect1">请登录</label>
        <br>
        <span>用户名:</span>
        <br>
        <input type="text" text name="username" v-model="form.username" />
        <br>
        <span>密码:</span>
        <br>
        <input type="password" text name="pwd" v-model="form.password" />
    </div>
    <button type="button" class="btn btn-primary" @click="postLogin">登录</button>
</form>
</template>

<script>
import axios from 'axios';
export default {
  name: "login",
  data() {
    return {
      form: {
        username: null,
        password: null
      }
    }
  },
  methods: {
    postLogin:function() {
      console.log(this.form)
      axios.get('/user/auth/',this.form,{withCredentials:true}).then((res)=> {
      console.log(res);
        // this.$router.go({path:'/'});
      });
    }
  }
}
</script>

<style scoped>
.login {
  width: 50%;
  margin: 0 auto;
}
span {
  text-align: left;
}
</style>
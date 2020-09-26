<template>
  <div id="app" class='container'>
    <nav class="navbar navbar-expand-sm navbar-light bg-light">
      <router-link class="nav-brand" to="/" >梁永光</router-link>

      <!-- 无法用 -->
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav">
        <span class="navbar-toggler-icon"></span>
      </button>


      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <router-link class="nav-link" to="/" >Home</router-link>
          <router-link class="nav-link" to="/about" >About</router-link>
          <router-link class="nav-link" to="/test">BI</router-link>

          <!-- 无法用 -->
          <div class="nav-link nav-item dropdown">
            <a href="#" class="nav-link dropdown-toggle" data-toggle="dropdown"> 下拉菜单</a>
            <div class="dropdown-menu">
              <router-link class="dropdown-item" to="/" >Home</router-link>
              <router-link class="dropdown-item" to="/about" >About</router-link>
              <router-link class="dropdown-item" to="/test">BI</router-link>
            </div>
          </div>


        </ul>
      </div>
    </nav>

    <nav class='nav nav-tabs'>
      <router-link class="nav-link" to="/" >Home</router-link>
      <router-link class="nav-link" to="/todo" >Todo</router-link>
      <router-link class="nav-link" to="/test">BI</router-link>
    </nav>
    <router-view/>
  </div>
</template>
<script>

</script>>

<style>
 #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

/*
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
} */
</style>

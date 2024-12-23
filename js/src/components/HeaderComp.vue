<template>
    <nav>
      <router-link to="/">Home</router-link>
      <router-link to="/add">Add Student</router-link>
      <a href="" @click="logout">Log Out</a>
    </nav>
 
</template>

<script>

    export default{
        name:'HeaderComp',

        methods:{
            logout(){
                this.$router.push({name:"Login"})
                localStorage.clear()
            }
        }


    }
</script>

<style>

</style>

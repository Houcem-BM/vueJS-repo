<template>
  <div class="container">
    <img src="../assets/logo.jpg" class="logo" />
    <h1>Sign Up</h1>
    <form>
      <input
        type="text"
        placeholder="Username"
        name="username"
        v-model="username"
        required
      />
      <input
        type="email"
        placeholder="Email"
        name="email"
        v-model="email"
        :class="{ 'input-error': emailError }"
        required
      />
      <p v-if="emailError" class="error-message">Email already exists</p>
      <input
        type="password"
        placeholder="Password"
        v-model="password"
        name="password"
        required
      />
      <button type="button" v-on:click="signup">Sign Up</button>
      <span>Already have an account?</span>
      <router-link to="/login">Login</router-link>
    </form>
  </div>
</template>

<script>
export default {
  name: "SignUp",
  data() {
    return {
      username: "",
      email: "",
      password: "",
      emailError: false,
    };
  },
  methods: {
    async signup() {
      //this.emailError = false;
      const response = await fetch("http://localhost:8000/users/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          userName: this.username,
          email: this.email,
          password: this.password,
        }),
      });
      //const data = await response.json();
      if (response.status != 200) {
        this.emailError = true;
      }else{
        localStorage.setItem("user", this.username)
        this.$router.push({name:'Home'})
      }
    },
  },
  mounted(){
      if (localStorage.getItem('user')){
        this.$router.push({name:'Home'})
      }
    }
};
</script>

<style>

</style>

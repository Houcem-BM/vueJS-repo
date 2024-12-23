<template>
  <div class="container">
    <img src="../assets/logo.jpg" class="logo" />
    <h1>Login</h1>
    <form>
      <input
        type="email"
        placeholder="Email"
        name="email"
        v-model="email"
        :class="{ 'input-error': emailError }"
        required
      />
      <p v-if="emailError" class="error-message">Email Not exists</p>
      <input
        type="password"
        placeholder="Password"
        name="password"
        v-model="password"
        :class="{ 'input-error': passwordError }"
        required
      />
      <p v-if="passwordError" class="error-message">Password Incorrect</p>

      <button @click="Login" type="button">Login</button>
      <span>You don't have an account?</span>
      <router-link to="/">Sign Up</router-link>
    </form>
  </div>
</template>

<script>
export default {
  name: "LoginPage",
  data() {
    return {
      email: "",
      password: "",
      emailError: false,
      passwordError: false,
    };
  },
  methods: {
    async Login() {
      const encodedEmail = encodeURIComponent(this.email);
      const encodedPassword = encodeURIComponent(this.password);

      const response = await fetch(
        `http://localhost:8000/users/${encodedEmail}/${encodedPassword}`,
        {
          method: "GET", // or "POST", "PUT", etc.
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      const data = await response.json();
      console.log(data)
      if (response.ok) {
        localStorage.setItem("user", data[0].name);
        this.$router.push({ name: "Home" });
      } else if (data.detail == "Email Not Exist") {
        this.emailError = true;
      } else {
        this.passwordError = true;
      }
    },
  },
  mounted() {
      let user = localStorage.getItem("user");
      if (user) {
        this.$router.push({ name: "Home" });
      }
    },
};
</script>

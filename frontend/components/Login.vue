<template>
  <div>
    <input v-model="username" type="text" placeholder="Username" />
    <input v-model="password" type="password" placeholder="Password" />
    <button @click="login()">Log In</button>
  </div>
</template>
<script>
export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    login() {
      this.$axios.post('/api/login/', {
        username: this.username,
        password: this.password,
      })
    },
  },
}
</script>

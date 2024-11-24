<!-- Toast.vue -->
<template>
  <div class="toast-container">
    <TransitionGroup name="toast">
      <div
        v-for="toast in toasts"
        :key="toast.id"
        :class="['toast-item', `toast-${toast.type}`]"
      >
        <div class="toast-content">
          <div class="toast-icon">
            <div v-if="toast.type === 'success'" class="success-icon">✅</div>
            <div v-else-if="toast.type === 'error'" class="error-icon">⛔️</div>
            <div v-else class="info-icon">ℹ️</div>
          </div>
          <p class="toast-message">{{ toast.message }}</p>
        </div>
      </div>
    </TransitionGroup>
  </div>
</template>

<script>
export default {
  name: 'Toast',
  data() {
    return {
      toasts: [],
      nextId: 0
    }
  },
  methods: {
    showToast(message, type = 'success') {
      const id = this.nextId++
      this.toasts.push({ id, message, type })
      setTimeout(() => {
        this.removeToast(id)
      }, 3000)
    },
    removeToast(id) {
      const index = this.toasts.findIndex(toast => toast.id === id)
      if (index > -1) {
        this.toasts.splice(index, 1)
      }
    }
  }
}
</script>

<style scoped>
.toast-container {
  position: fixed;
  top: 20px;
  right: 20px;
  z-index: 99999;
}

.toast-item {
  margin-bottom: 10px;
  padding: 15px;
  border-radius: 4px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
  min-width: 300px;
  max-width: 400px;
}

.toast-content {
  display: flex;
  align-items: center;
}

.toast-icon {
  margin-right: 10px;
  font-size: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
}

.toast-message {
  margin: 0;
  font-size: 14px;
  font-weight: 500;
}

.toast-success {
  background-color: white;
  color: black;
}

.toast-error {
  background-color: white;
  color: black;
}

.toast-info {
  background-color: white;
  color: black;
}

.success-icon, .error-icon, .info-icon {
  color: white;
}
/* 애니메이션 */
.toast-enter-active,
.toast-leave-active {
  transition: all 0.5s ease;
}

.toast-enter-from {
  opacity: 0;
  transform: translateX(100%);
}

.toast-leave-to {
  opacity: 0;
  transform: translateX(100%);
}
</style>
<template>

  <header class="navbar navbar-dark sticky-top">
    <div class="nav navbar pt-2">
      <div class="navbar-brand shadow-none d-flex align-items-center">
        <img class="navbar-logo" src="@/assets/favicon.png" />
      </div>
    </div>

    <Toast ref="toast" />

    <!-- Center Section with About Us & Shops Links -->
    <div class="center-container">
      <div class="shops" @click="closeAboutUs">SHOPS</div>
      <div class="aboutUs" @click="toggleAboutUs">ABOUT US</div>
    </div>

    <div class="right-container">
      <img 
        class="order-status" 
        src="@/assets/orderStatus.png" 
        alt="Status" 
        @click="showOrderStatus" 
      />
      <!-- 로그인한 상태에서는 유저의 이름과 로그아웃 버튼을 표시 -->
      <div v-if="isLoggedIn" class="user-info">
        <span class="username">{{ username }}</span>
        <img class="user-logo" src="@/assets/user.png" alt="User" @click="toggleProfileModal" />
      </div>

      <!-- 로그인되지 않은 상태에서는 로그인 아이콘 표시 -->
      <div v-else class="login" @click="toggleLogin">
        <img class="login-logo" src="@/assets/log-in.png" alt="Login"/>
      </div>
      <div class="shopping-cart" @click="$emit('open-cart')">
        <span v-if="cartItemCount" class="cart-item-count">{{ cartItemCount }}</span>
        <img class="shopping-cart-logo" src="@/assets/shopping-cart-icon.png" alt="Shopping Cart" />
      </div>
    </div>


    <!-- About Us Modal -->
    <div v-if="showAboutUs" class="about-modal-overlay" @click.self="toggleAboutUs">
      <div class="categories-modal-content modal-content">
        <img class="close-btn" src="@/assets/close-button.png" @click="toggleAboutUs" />
        <section class="categories" id="categories">
          <div class="center-text">
            <strong>Categories</strong>
            <h2>Explore Culinary Delights</h2>
          </div>
          <div ref="categoriesContainer" class="categories-content">
            <div class="box">
              <div class="box-img">
                <img src="@/assets/images/categories/food.webp" loading="lazy" width="501px" height="500px" alt="Grilled steak served with a fresh garden salad and a side of mayonnaise">
              </div>
              <h3>World Bites</h3>
              <p>Experience global flavors with our International Delights, a curated journey through diverse cuisines that transport your taste buds.</p>
            </div>
            <div class="box">
              <div class="box-img">
                <img src="@/assets/images/categories/burger.webp" loading="lazy" width="600px" height="600px" alt="Close-up of a cheeseburger with lettuce, tomato, onion, pickles, and a sesame seed bun">
              </div>
              <h3>Gourmet Burgers</h3>
              <p>Elevate your burger experience with our Gourmet Burgers, crafted with premium ingredients for a unique and savory taste adventure.</p>
            </div>
            <div class="box">
              <div class="box-img">
                <img src="@/assets/images/categories/pastries.webp" loading="lazy" width="512px" height="512px" alt="Plate of assorted pastries and donuts with various toppings and decorations">
              </div>
              <h3>Sweet Temptations</h3>
              <p>Indulge in Sweet Temptations, a paradise of heavenly pastries and desserts that promise to delight your senses.</p>
            </div>
          </div>
        </section>

        <section class="history" id="history">
          <div ref="historyImg" class="history-img">
              <img src="@/assets/images/pizza.webp"
                  loading="lazy"
                  width="400px"
                  height="315px"
                  alt="">
          </div>

          <div ref="historyText" class="history-text">
              <h1 class="history-title">Our History</h1>
              <h2>Discover Our Glory begenning</h2>
              <p>We promise you'll enjoy every sweet moment to find your favourite. Eat what you love and save your time.</p>
              <a href="#" class="btn">Learn More</a>
          </div>
        </section>

        <section class="services" id="services">
          <div class="center-text">
              <h1 class="services-title">Offering</h1>
              <h2 class="service-subtitle">Our amazing services</h2>
          </div>
          
          <div ref="servicesContainer" class="services-container">
              <div class="services-content">
                  <img class="services-img" src="@/assets/images/services/dish.png" loading="lazy" alt="dish icon">
                  <h3 class="services-title">Excellent food</h3>
                  <p class="services-description">Savor the excellence in every bite at our establishment. Our chefs craft each dish with precision, delivering a delightful culinary experience that sets the standard for quality.</p>
              </div>

              <div class="services-content">
                  <img class="services-img" src="@/assets/images/services/pizza.png" loading="lazy" alt="pizza icon">
                  <h3 class="services-title">Fast food</h3>
                  <p class="services-description">Experience quick and satisfying flavors with our fast food service. Enjoy deliciousness on the go without compromising speed. Taste the convenience of a swift culinary journey.</p>
              </div>

              <div class="services-content">
                  <img class="services-img" src="@/assets/images/services/truck.png" loading="lazy" alt="truck icon">
                  <h3 class="services-title">Delivery</h3>
                  <p class="services-description">Bringing exceptional flavors to your doorstep, our delivery service ensures a seamless and flavorful experience. Enjoy our delectable creations from the comfort of your home, delivered with reliability and convenience.</p>
              </div>
          </div>
        </section>
      </div>
    </div>

    <!-- Login/Signup Modal -->
    <div v-if="showLogin" class="login-modal-overlay" @click.self="toggleLogin">
      <div class="auth-form modal-content">
        <img class="close-btn" src="@/assets/close-button.png" @click="toggleLogin"/>
        <h3>{{showSignup ? 'Sign Up' : 'Login'}}</h3>
        <form @submit.prevent="handleAuthSubmit">
          <input 
            v-if="showSignup" 
            type="text" 
            placeholder="Full Name" 
            v-model="fullName" 
            required
          />
          <input 
            type="text" 
            placeholder="Username" 
            v-model="username" 
            required
          />
          <input 
            v-if="showSignup" 
            type="email" 
            placeholder="Email" 
            v-model="email" 
            required
          />
          <input 
            type="password" 
            placeholder="Password" 
            v-model="password" 
            required
          />
          <input 
            v-if="showSignup" 
            type="password" 
            placeholder="Confirm Password" 
            v-model="confirmPassword" 
            required
          />
          <button type="submit">
            {{ showSignup ? 'Sign up' : 'Login' }}
          </button>
        </form>
        
        <button class="toggle-btn" @click="toggleSignup">
          {{ showSignup ? "Already have an account? Login" : "Don't have an account? Sign Up" }}
        </button>
      </div>
    </div>
    
    <!-- Profile Modal -->
    <div v-if="showProfileModal" class="profile-modal-overlay" @click.self="toggleProfileModal">
      <div class="profile-modal modal-content">
        <img class="close-btn" src="@/assets/close-button.png" @click="toggleProfileModal"/>
        <p class="profile">Profile</p>
        <img class="user-logo" src="@/assets/user.png" alt="User"/>
        <p>{{ username }}</p>
        <button @click="openEditProfile" class="editProfile-btn">Edit Profile</button>
        <button @click="logout" class="loggedin-logout-btn">Logout</button>
      </div>
    </div>

    <!-- Edit Profile Modal -->
    <div v-if="showEditProfileModal" class="edit-modal-overlay" @click.self="closeEditProfile">
      <div class="edit-profile-modal modal-content">
        <img class="close-btn" src="@/assets/close-button.png" @click="closeEditProfile"/>
        <h3 class="editProfile">Edit Profile</h3>
        <form @submit.prevent="handleEditProfile" class="handleEditProfile">
          <p class="newUsername">New Username</p>
          <input type="text" placeholder="New Username" v-model="newUsername" required/>
          <p class="newEmail">New Email</p>
          <input type="email" placeholder="New Email" v-model="newEmail" required/>
          <p class="newPassword">New Password</p>
          <input type="password" placeholder="New Password" v-model="newPassword" required/>
          <div class="saveOrCancle-btn">
            <button type="submit" class="saveChanges">Save Changes</button>
            <button class="cancle" @click="closeEditProfile">Cancel</button>
          </div>
        </form>
      </div>
    </div>

     <!-- Order Status Modal -->
     <div v-if="showOrderStatusModal" class="order-status-modal">
      <div class="modal-content">
        <!-- Close Button -->
        <img class="close-button" src="@/assets/close-button.png" @click="closeOrderStatusModal" alt="Close" />
        
        <!-- Order Number -->
        <div class="order-number">
          <p><b>Order #{{ randomOrderId }}</b></p>
        </div>
        
        <!-- Order Status Steps -->
        <div class="order-status-steps">
          <div 
            v-for="(step, index) in orderSteps" 
            :key="index" 
            class="order-step"
          >
            
            <!-- Status Circle -->
            <div 
              class="status-circle"
              :class="{
                completed: step.status === 'completed',
                pending: step.status === 'pending',
              }"
            >
              <img src="@/assets/check.png" alt="Step Status" />
            </div>
            
            <!-- Step Label -->
            <p>{{ step.label }}</p>
          </div>
        </div>
        
        <!-- Order Status Progression -->
        <div class="order-status-progression">
          <template v-for="(step, index) in orderSteps" :key="index">
            <div 
              v-if="step.status === 'completed'" 
              class="order-details"
            >
              <img src="@/assets/statusIcon.png" alt="Order Status Icon" class="status-icon" />
              <div class="order-info">
                <p class="order-label"><b>{{ step.statusDescription }}</b></p>
                <p class="order-timestamp">{{ formatTimestamp(orderTimestamps[step.timestampKey]) }}</p>
              </div>
            </div>
          </template>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
import "../styles/navbar.css"
import "../styles/shoppingcart.css"
import "../styles/auth.css"
import "../styles/aboutUs.css"
import "../styles/profile.css"
import "../styles/orderStatus.css"
import Toast from './Toast.vue'
import axios from "axios";

export default {
  name: "NavBar",
  components: {
    Toast
  },
  props: {
    shoppingCart: {
      type: Array,
      default: () => [],
    },
    orderTimestamps: {
      type: Object,
      default: () => ({
        orderAccepted: null,
        cookingStarted: null,
        deliveryStarted: null,
        orderArrived: null
      })
    }
  },
  data() {
    return {
      showLogin: false,
      showSignup: false,
      showAboutUs: false,
      isLoggedIn: false,
      showProfileModal: false,
      showEditProfileModal: false,
      username: '',
      password: '',
      email: '',
      fullName: '',
      confirmPassword: '',
      newUsername: '',
      newPassword: '',
      token: null,
      showOrderStatusModal: false,
      orderSteps: [
        {
          label: 'Accepted',
          status: this.orderTimestamps.orderAccepted ? 'completed' : 'pending',
          statusDescription: 'Order accepted at the store',
          timestampKey: 'orderAccepted'
        },
        {
          label: 'Cooking',
          status: this.orderTimestamps.cookingStarted ? 'completed' : 'pending',
          statusDescription: 'Cooking started at the store',
          timestampKey: 'cookingStarted'
        },
        {
          label: 'Delivery',
          status: this.orderTimestamps.deliveryStarted ? 'completed' : 'pending',
          statusDescription: 'Delivery started',
          timestampKey: 'deliveryStarted'
        },
        {
          label: 'Arrived',
          status: this.orderTimestamps.orderArrived ? 'completed' : 'pending',
          statusDescription: 'Order has arrived',
          timestampKey: 'orderArrived'
        }
      ],
      randomOrderId:  Math.random().toString(36).substr(2, 6).toUpperCase(), 
    }
  },
  computed: {
    cartItemCount() {
      return this.shoppingCart.length;
    },
  },
  created() {
    // Check for existing token
    const token = localStorage.getItem('token');
    if (token) {
      this.token = token;
      this.isLoggedIn = true;
      this.username = localStorage.getItem('username');
    }
  },
  watch: {
    orderTimestamps: {
      deep: true,
      handler(newTimestamps) {
        this.updateOrderSteps(newTimestamps);
      }
    }
  },
  methods: {
    handleAuthSubmit(event) {
    event.preventDefault();
    if (this.showSignup) {
      this.handleSignup(event);
    } else {
      this.handleLogin(event);
    }
    },

    toggleAuthMode() {
      // 모드 전환 전에 이전 이벤트 리스너 제거
      this.removeAuthEventListeners();
      this.showSignup = !this.showSignup;
      this.resetForm();
      
      if (this.$refs.toast) {
        //this.$refs.toast.clearToast();
      }
    },
    removeAuthEventListeners() {
      const form = document.querySelector('.auth-form form');
      if (form) {
        console.log('Removing event listeners');
        form.removeEventListener('submit', this.handleLogin);
        form.removeEventListener('submit', this.handleSignup);
      }
    },

    toggleLogin() {
      this.showLogin = !this.showLogin;
      this.showSignup = false;
      this.resetForm();
    },

    toggleSignup() {
      this.showSignup = !this.showSignup;
      this.showLogin = true;
      this.resetForm();
    },

    toggleAboutUs() {
      this.showAboutUs = !this.showAboutUs;
    },
    closeAboutUs() {
      this.showAboutUs = false;
    },

    async handleSignup(event) {
      event.preventDefault();
      console.log('Signup process started'); 
     
      
      if (!this.username || !this.fullName || !this.email || !this.password) {
        this.$refs.toast.showToast('All fields are required', 'error');
        return;
      }

      if (this.password !== this.confirmPassword) {
        this.$refs.toast.showToast('Passwords do not match', 'error');
        return;
      }

      const formData = new FormData();
        formData.append('username', this.username);
        formData.append('email', this.email);
        formData.append('fullname', this.fullName);
        formData.append('password', this.password);

      try {
        console.log("-------------------------------------- start")
        await axios.post('http://localhost:8080/api/register', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
        console.log("-------------------------------------- end")

        console.log('Signup response:', response.data); 

        const { access_token, token_type } = response.data;
        this.token = access_token || response.data.token; 
        localStorage.setItem('token', access_token);
        localStorage.setItem('username', this.username);
        
        this.isLoggedIn = true;
        //await this.fetchUserProfile();
        
        this.$refs.toast.showToast('Account created and logged in successfully!', 'success');
        this.showLogin = false;
        this.showSignup = false;
        this.resetForm();
      } catch (error) {
          console.error('Signup error:', error.response?.data);
          const errorMessage = error.response?.data?.detail || 'Registration failed';
          this.$refs.toast.showToast(errorMessage, 'error');
      }
    },

    async handleLogin(event) {
      event.preventDefault();
      console.log('Login process started'); 
      const formData = new FormData();
      formData.append('username', this.username);
      formData.append('password', this.password);

      try {
        const response = await axios.post('http://localhost:8080/api/login', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        console.log('Login response:', response.data);

        const { access_token, token_type } = response.data;
        this.token = access_token;
        localStorage.setItem('token', access_token);
        
        this.isLoggedIn = true;
        this.username = this.username;
        
        this.$refs.toast.showToast(`Welcome back, ${this.username}!`, 'success');
        this.showLogin = false;
        this.resetForm();
      } catch (error) {
        console.error('Login error:', error);
        const errorMessage = error.response?.data?.detail || 'Invalid username or password';
        this.$refs.toast.showToast(errorMessage, 'error');
      }
    },

    resetForm() {
      this.username = '';
      this.password = '';
      this.email = '';
      this.fullName = '';
      this.confirmPassword = '';
    },

    logout() {
      this.isLoggedIn = false;
      this.token = null;
      localStorage.removeItem('token');
      this.username = '';
      this.showProfileModal = false;
      this.showEditProfileModal = false;
      this.$refs.toast.showToast('Logged out successfully', 'success');
    },
    toggleProfileModal() {
      this.showProfileModal = !this.showProfileModal;
    },

    openEditProfile() {
      this.showProfileModal = false;
      this.showEditProfileModal = true;
    },

    closeEditProfile() {
      this.showEditProfileModal = false;
      this.showProfileModal = true;
    },

    async handleEditProfile() {
      const formData = new FormData();
      if (this.newUsername) formData.append('username', this.newUsername);
      if (this.newEmail) formData.append('email', this.newEmail);
      if (this.newPassword) formData.append('password', this.newPassword);

      try {
        await axios.put('http://localhost:8080/api/updateProfile', formData, {
          headers: {
            'Authorization': `Bearer ${this.token}`,
            'Content-Type': 'multipart/form-data',
          }
        });

        if (this.newUsername) {
          this.username = this.newUsername;
          localStorage.setItem('username', this.newUsername);
        }
        if (this.newEmail) {
          this.email = this.newEmail;
          localStorage.setItem('email', this.newEmail);
        }
        if (this.newPassword) {
          this.password = this.newPassword;
          localStorage.setItem('password', this.newPasswird);
        }


        this.$refs.toast.showToast('Profile updated successfully', 'success');
        this.closeEditProfile();
        this.newUsername = '';
        this.newPassword = '';
        this.newEmail = '';
      } catch (error) {
        console.error('Profile update error:', error.response?.data);
        const errorMessage = error.response?.data?.detail || 'Failed to update profile';
        this.$refs.toast.showToast(errorMessage, 'error');
      }
    },
    closeEditProfile() {
      this.showEditProfileModal = false;
      this.showProfileModal = true; 
    },

    showOrderStatus() {
      this.showOrderStatusModal = true;
    },
    closeOrderStatusModal() {
      this.showOrderStatusModal = false;
    },
    formatTimestamp(timestamp) {
      return timestamp ? new Date(timestamp).toLocaleString() : '';
    },
    updateOrderSteps(timestamps) {
      // Update order status by following timestamps

      // Accept order
      this.orderSteps[0].status = timestamps.orderAccepted 
        ? "completed" 
        : "pending";
      
      // Start cooking
      this.orderSteps[1].status = timestamps.cookingStarted 
        ? "completed" 
        : (timestamps.orderAccepted ? "pending" : "pending");
      
      // Start deliverying
      this.orderSteps[2].status = timestamps.deliveryStarted 
        ? "completed" 
        : (timestamps.cookingStarted ? "pending" : "pending");
      
      // Arrived
      this.orderSteps[3].status = timestamps.orderArrived 
        ? "completed" 
        : (timestamps.deliveryStarted ? "pending" : "pending");
    },
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Doto:wght@100..900&family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700;1,900&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&family=Short+Stack&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Doto:wght@100..900&family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700;1,900&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&family=Short+Stack&family=Walter+Turncoat&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Doto:wght@100..900&family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700;1,900&family=Noto+Sans+SC:wght@100..900&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&family=Short+Stack&family=Walter+Turncoat&display=swap');

.center-container { 
  display: flex; 
  justify-content: center; 
  align-items: center; 
  gap: 30px;
}

.shops, .aboutUs {
  font-size: 1.2rem;
  color: rgb(32, 32, 61);
  font-weight: 550;
}

.shops, .aboutUs:hover {
  font-size: 1.2rem;
  color: rgb(73, 73, 127);
  font-weight: 550;
}

.order-status {
  height: 23px;
  width: 23px;
}

/* Common modal overlays */
.edit-modal-overlay,
.profile-modal-overlay,
.login-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Specific styles for the About Us modal */
.about-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100%;
  height: 100%;
  backdrop-filter: blur(10px);
  background-color: rgba(255, 255, 255, 0.4);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10;
}

.order-status-modal >>> .modal-content {
  width: 43% !important; 
  max-width: 800px !important;
}

.close-btn {
  position: absolute;
  top: 10px;
  right: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}


.modal-content {
  background: #fff;
  padding: 30px;
  border-radius: 10px;
  text-align: center;
  width: 400px; 
  max-width: 90%; 
}

.categories-modal-content {
  background-color: #ffffff;
  padding: 12px;
  border-radius: 10px;
  width: 95%;
  max-width: 1500px;
  height: 90%;
  overflow-y: auto;
  position: relative;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
</style> 
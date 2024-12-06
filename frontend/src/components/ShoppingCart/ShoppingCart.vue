<template>
  <Toast ref="toast" />

  <div class="shopping-cart-container">
    <div class="shopping-cart-header sticky-top">
      <button class="close-btn" @click="closeFrame">
        <span>&times;</span>
      </button>
      <h3>Shopping Cart</h3>
      <hr/>
    </div>
    <div class="shopping-cart-body">
      <food-item
      v-for="(item, index) in shoppingCart"
      :key="index"
      :food="item"
      :view="'shoppingcart'"
      @remove-from-cart="removeFromCart"
      :class="{ 'fade-away': item.fadeAway }"
      @register-action="registerAction"
    ></food-item>
    </div>
    <div v-if="shoppingCart.length">
      <hr/>
      <div class="shopping-cart-footer sticky-bottom" v-if="!isLoading && !orderStatus">
        <p class="total-price-container">Tổng giá: {{ totalPrice.toFixed(2) }} $</p>
        <button @click="submitOrder" class="order-btn">Đặt hàng</button>
      </div>
    </div>

    
    <div class="shopping-cart-footer sticky-bottom" v-if="isLoading || orderStatus" style="animation: fadeInSlideUp 0.5s ease forwards">
      <p>{{ this.placeholderMsg }}</p>
      <loading-spinner v-if="isLoading" ></loading-spinner>
    </div>
    
  </div>
</template>

  <script>
  import "../styles/shoppingcart.css"
  import FoodItem from "../Common/FoodItem.vue"
  import LoadingSpinner from "../Common/LoadingSpinner.vue"
  import Toast from "../NavBar/Toast.vue"

  export default {
    components: {
      FoodItem,
      LoadingSpinner,
      Toast
    },    
    props: {
      shoppingCart: {
        type: Array,
        default: () => [],
      },
    },
    data() {
      return {
        isLoading: false,
        orderStatus: false,
        //placeholderMsg: "Placing your order...",
        placeholderMsg: "Đang đặt hàng của bạn...",
        orderTimestamps: {
          orderAccepted: null,
          cookingStarted: null,
          deliveryStarted: null,
          orderArrived: null
        }
      }
    },
    computed: {
      totalPrice() {
        return this.shoppingCart.reduce(
          (total, item) => total + item.price * item.quantity,
          0
        );
      },
    },
    methods: {
      toggleAuthMode() {
        // 토스트 알림 초기화
        if (this.$refs.toast) {
          this.$refs.toast.clearToast();
        }
      },
      registerAction(msg) {
        this.$emit("register-action", msg)
      },
      closeFrame() {
        this.$emit('close-cart')
        //this.placeholderMsg = "Placing your order..."
        this.placeholderMsg = "Đang đặt hàng của bạn..."
        this.isLoading = false
        this.orderStatus = false
        
      },
      clearCart() {
        this.$emit('clear-shopping-cart')
      },
      removeFromCart(item) {
        this.$emit('remove-from-cart', item)
      },
      orderStatus() {
        this.$emit('order-status')
      },
      submitOrder() {
      this.isLoading = true;
      //this.placeholderMsg = "Placing your order..."
      this.placeholderMsg = "Đang đặt hàng của bạn..."
      
      setTimeout(() => {
        this.isLoading = false;
        //this.placeholderMsg = "Your order has been sent..."
        this.placeholderMsg = "Đơn hàng của bạn được gửi rồi..."
        this.orderStatus = true // Sent order
        this.clearCart()

        // 주문 제출 이벤트 emit
        this.$emit('order-submit');
      }, 2500);

        //this.placeholderMsg = "Place your order..."
        this.placeholderMsg = "Đang đặt hàng của bạn..."
        this.registerAction("placed the order as is")
      },
    // ...
    },
  };
  </script>
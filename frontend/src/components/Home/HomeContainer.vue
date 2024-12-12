<template>
  <div class="home-container">
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
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style scoped>
.home-container {
  width: 100%;
  min-height: 100vh;
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #f5f5f5; /* hoặc màu nền tùy chọn */
}
</style> 
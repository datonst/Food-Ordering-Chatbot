<template>
  <div class="home-container">
    <section class="categories" id="categories">
      <div class="center-text">
        <strong>Danh Mục</strong>
        <h2>Khám Phá Những Món Ngon</h2>
      </div>
      <div ref="categoriesContainer" class="categories-content">
        <div class="box">
          <div class="box-img">
            <img src="@/assets/images/categories/food.webp" loading="lazy" width="501px" height="500px" alt="Bít tết nướng phục vụ cùng salad tươi và sốt mayonnaise">
          </div>
          <h3>Hương Vị Thế Giới</h3>
          <p>Trải nghiệm các hương vị toàn cầu với các món ngon quốc tế, một hành trình khám phá ẩm thực đa dạng, đưa bạn đến với những món ăn đặc sắc từ khắp nơi trên thế giới.</p>
        </div>
        <div class="box">
          <div class="box-img">
            <img src="@/assets/images/categories/burger.webp" loading="lazy" width="600px" height="600px" alt="Close-up of a cheeseburger with lettuce, tomato, onion, pickles, and a sesame seed bun">
          </div>
          <h3>Burger Thượng Hạng</h3>
          <p>Nâng tầm trải nghiệm burger của bạn với những chiếc burger thượng hạng, chế biến từ nguyên liệu cao cấp mang đến hương vị độc đáo và thơm ngon.</p>
        </div>
        <div class="box">
          <div class="box-img">
            <img src="@/assets/images/categories/pastries.webp" loading="lazy" width="512px" height="512px" alt="Đĩa bánh ngọt và bánh donut với nhiều loại nhân và trang trí khác nhau">
          </div>
          <h3>Mê Mẩn Ngọt Ngào</h3>
          <p>Thỏa sức thưởng thức những chiếc bánh ngọt tuyệt vời, nơi vương quốc của các món tráng miệng với hương vị ngọt ngào, tươi mới sẽ khiến bạn không thể cưỡng lại.</p>
        </div>
      </div>
    </section>

    <section class="history" id="history">
      <div ref="historyImg" class="history-img">
          <img src="@/assets/images/pizza.webp"
              loading="lazy"
              width="400px"
              height="315px"
              alt="Món pizza ngon lành">
      </div>

      <div ref="historyText" class="history-text">
          <h1 class="history-title">Lịch Sử Của Chúng Tôi</h1>
          <h2>Khám Phá Chặng Đường Thành Công</h2>
          <p>Chúng tôi cam kết sẽ mang đến những khoảnh khắc ngọt ngào cho bạn, giúp bạn dễ dàng tìm thấy món ăn yêu thích và tiết kiệm thời gian hơn bao giờ hết.</p>
          <a href="#" class="btn">Tìm Hiểu Thêm</a>
      </div>
    </section>

    <section class="services" id="services">
      <div class="center-text">
          <h1 class="services-title">Dịch Vụ</h1>
          <h2 class="service-subtitle">Những dịch vụ tuyệt vời của chúng tôi</h2>
      </div>
      
      <div ref="servicesContainer" class="services-container">
          <div class="services-content">
              <img class="services-img" src="@/assets/images/services/dish.png" loading="lazy" alt="Biểu tượng món ăn">
              <h3 class="services-title">Món Ăn Xuất Sắc</h3>
              <p class="services-description">Thưởng thức sự xuất sắc trong từng miếng ăn tại nhà hàng của chúng tôi. Những món ăn được chế biến tỉ mỉ mang đến trải nghiệm ẩm thực hoàn hảo, làm chuẩn mực cho chất lượng.</p>
          </div>

          <div class="services-content">
              <img class="services-img" src="@/assets/images/services/pizza.png" loading="lazy" alt="Biểu tượng pizza">
              <h3 class="services-title">Đồ Ăn Nhanh</h3>
              <p class="services-description">Trải nghiệm hương vị nhanh chóng và thỏa mãn với dịch vụ đồ ăn nhanh. Đắm chìm trong những món ăn thơm ngon, đầy đủ chất lượng mà không phải chờ đợi lâu.</p>
          </div>

          <div class="services-content">
              <img class="services-img" src="@/assets/images/services/truck.png" loading="lazy" alt="Biểu tượng xe giao hàng">
              <h3 class="services-title">Giao Hàng Tận Nơi</h3>
              <p class="services-description">Mang đến những món ăn tuyệt vời ngay tại nhà bạn, dịch vụ giao hàng của chúng tôi đảm bảo mang đến trải nghiệm ẩm thực tuyệt hảo mà bạn không cần rời khỏi nhà.</p>
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
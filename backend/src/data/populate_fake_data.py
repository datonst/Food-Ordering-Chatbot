import pandas as pd
from sqlalchemy.orm import Session

from database import SessionLocal
from data_models import Restaurant, Foods, Users

def add_restaurant(db: Session, name: str, description: str, image: str):
    existing_res = db.query(Restaurant).filter(Restaurant.name == name).first
    # if existing_res:
    #     print(f"Restaurant with name {name} already exist")
    #     return existing_res
    restaurant = Restaurant(name=name, description=description, image=image)
    db.add(restaurant)
    db.commit()
    db.refresh(restaurant)
    return restaurant

def add_food(db: Session, restaurant_id: int, name: str, description: str, image: str, price: int):
    exist_food = db.query(Foods).filter(Foods.name == name).first
    food = Foods(restaurant_id=restaurant_id, name=name, description=description, image=image, price=price)
    db.add(food)
    db.commit()
    db.refresh(food)
    return food

def add_user(db: Session, id: int, username: str, fullname: str, email: str, password: str):
    existing_user = db.query(Users).filter(Users.username == username).first()
    if existing_user:
        print(f"User with username {username} already exist")
        return existing_user 
    existing_user = db.query(Users).filter(Users.email == email).first()
    if existing_user:
        print(f"User with email {email} already exists.")
        return existing_user 
    user = Users(id = id, username = username, fullname = fullname, email = email, password = password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def main():
    db = SessionLocal()

    # Sample data for restaurants
    restaurants = [
            {"name": "Nhà hàng ngon", "description": "Chuyên các món Việt truyền thống với không gian ấm cúng, phù hợp gia đình và khách du lịch", "image": "restaurants/nha_hang_ngon.png"},
            {"name": "Cơm Tấm Mộc", "description": "Chuyên cơm tấm sườn nướng thơm ngon, chuẩn vị miền Nam", "image": "restaurants/com_tam_moc.png"},
            {"name": "Quán Bún Bò Huế O Xuân", "description": "Bún bò Huế đậm đà hương vị miền Trung", "image": "restaurants/quan_bun_bo_hue_o_xuan.png"},
            {"name": "Nhà hàng Phố Biển", "description": "Hải sản tươi sống chế biến hấp dẫn, đậm vị biển cả", "image": "restaurants/nha_hang_pho_bien.png"},
            {"name": "Nhà hàng Hội An", "description": "Đặc sản miền Trung, mang phong cách phố cổ", "image": "restaurants/nha_hang_hoi_an.png"},
            {"name": "Nhà hàng Sen Tây Hồ", "description": "Buffet cao cấp với hàng trăm món ăn từ Á đến Âu, không gian sang trọng", "image": "restaurants/nha_hang_sen_tay_ho.png"},
            {"name": "Lẩu nấm Ashima", "description": "Lẩu nấm bổ dưỡng, phong cách ẩm thực Nhật Bản tinh tế", "image": "restaurants/lau_nam_ashima.png"},
            {"name": "Nhà hàng Sumo Yakiniku", "description": "Nướng lẩu Nhật Bản phong cách Yakiniku, nguyên liệu thượng hạng", "image": "restaurants/nha_hang_sumo_yakiniku.png"},
            {"name": "Quán Lẩu Phan", "description": "Lẩu buffet bình dân với nhiều mức giá, đa dạng món ăn", "image": "restaurants/quan_lau_phan.png"},
            {"name": "Nhà hàng Ngon Garden", "description": "Không gian vườn thoáng đãng, các món Việt truyền thống hấp dẫn", "image": "restaurants/nha_hang_ngon_garden.png"},
            {"name": "Nhà hàng Moo Beef Steak", "description": "Thịt bò nhập khẩu, chuyên các món steak đẳng cấp Âu Mỹ", "image": "restaurants/nha_hang_moo_beef_steak.png"},
            {"name": "Quán Nét Huế", "description": "Đặc sản miền Trung với không gian giản dị và gần gũi", "image": "restaurants/quan_net_hue.png"},
            {"name": "Nhà hàng Quán Ăn Ngon", "description": "Ẩm thực ba miền với hương vị truyền thống khó quên", "image": "restaurants/nha_hang_quan_an_ngon.png"},
            {"name": "Nhà hàng Al Fresco's", "description": "Pizza, pasta và món Tây ngon miệng trong không gian hiện đại", "image": "/restaurants/nha_hang_fresco.png"},
            {"name": "Nhà hàng Hẻm Quán", "description": "Ẩm thực đường phố với các món ăn dân dã, độc đáo", "image": "restaurants/nha_hang_hem_quan.png"},
            {"name": "Nhà hàng Gogi House", "description": "Thịt nướng Hàn Quốc chính gốc với nhiều món ăn kèm hấp dẫn", "image": "restaurants/nha_hang_gogi_house.png"},
            {"name": "Nhà hàng King BBQ", "description": "Buffet nướng Hàn Quốc với nước sốt bí truyền thơm ngon", "image": "restaurants/nha_hang_king_bbq.png"},
            {"name": "Nhà hàng Manwah", "description": "Lẩu Đài Loan tinh tế với nhiều loại nước dùng đặc trưng", "image": "restaurants/nha_hang_manwah.png"},
            {"name": "Nhà hàng Kichi-Kichi", "description": "Buffet lẩu băng chuyền đa dạng, phong cách hiện đại", "image": "restaurants/nha_hang_kichi_kichi.png"},
            {"name": "Nhà hàng Pepperonis", "description": "Pizza, pasta và các món Âu đơn giản nhưng ngon miệng", "image": "restaurants/nha_hang_pepperonis.png"},
            {"name": "Nhà hàng Ẩm Thực Việt", "description": "Các món Việt truyền thống với nguyên liệu tươi ngon", "image": "restaurants/nha_hang_am_thuc_viet.png"},
            {"name": "Nhà hàng Chả Cá Lã Vọng", "description": "Chả cá Hà Nội đặc sản với lịch sử hàng trăm năm", "image": "restaurants/nha_hang_cha_ca_la_vong.png"},
            {"name": "Nhà hàng Lẩu Cua Đồng", "description": "Lẩu cua đồng đậm vị đồng quê Việt Nam", "image": "restaurants/nha_hang_lau_cua_dong.png"},
            {"name": "Quán Bánh Xèo Ba Miền", "description": "Bánh xèo giòn rụm từ Bắc, Trung, Nam", "image": "restaurants/quan_banh_xem_ba_mien.png"},
            {"name": "Nhà hàng Tokyo Deli", "description": "Ẩm thực Nhật Bản với sushi, sashimi tươi ngon", "image": "restaurants/nha_hang_tokyo_deli.png"}
        ]

    # # Sample data for foods
    foods = [
  
        # Nhà hàng Ngon
        {"restaurant_id": 1, "name": "Gỏi cuốn tôm thịt", "description": "Rau sống tươi, bún, tôm và thịt, cuốn trong bánh tráng, ăn kèm nước mắm chua ngọt", "image": "foods/goi_cuon_tom_thit.png", "price": 9},
        {"restaurant_id": 1, "name": "Bánh xèo miền Nam", "description": "Bánh xèo vàng giòn, nhân tôm thịt, giá đỗ, chấm nước mắm pha", "image": "foods/banh_xeo_mien_nam.png", "price": 12},
        {"restaurant_id": 1, "name": "Chè ba màu", "description": "Đậu xanh, đậu đỏ, thạch lá dứa và nước cốt dừa mát lạnh", "image": "foods/che_ba_mau.png", "price": 7},
        {"restaurant_id": 1, "name": "Phở bò tái nạm", "description": "Nước dùng thanh ngọt, thịt bò tái mềm, ăn kèm bánh phở dai ngon", "image": "foods/pho_bo_tai_nam.png", "price": 9},
        {"restaurant_id": 1, "name": "Bánh khọt tôm tươi", "description": "Bánh nhỏ giòn, nhân tôm, dừa nạo, ăn kèm rau sống", "image": "foods/banh_khot_tom_tuoi.png", "price": 8},
        {"restaurant_id": 1, "name": "Bún riêu cua", "description": "Nước lèo đậm đà từ cua đồng, ăn cùng rau thơm và bún tươi", "image": "foods/bun_rieu_cua.png", "price": 5},
        {"restaurant_id": 1, "name": "Chả giò thịt heo", "description": "Chả giò vàng ruộm, nhân thịt heo và rau củ, giòn tan", "image": "foods/cha_gio_thit_heo.png", "price": 6},

        #Cơm Tấm Mộc
        {"restaurant_id": 2, "name": "Cơm tấm sườn non nướng", "description": "Sườn non ướp đậm vị, nướng thơm, ăn với cơm tấm nóng hổi", "image": "foods/com_tam_suon_non_nuong.png", "price": 13},
        {"restaurant_id": 2, "name": "Trứng ốp la cơm tấm", "description": "Trứng lòng đào mềm béo, ăn kèm cơm tấm", "image": "foods/trung_op_la_com_tam.png", "price": 7},
        {"restaurant_id": 2, "name": "Dưa chua ăn kèm", "description": "Dưa chua tự làm, chua nhẹ, giúp cân bằng món chính", "image": "foods/dua_chua_an_kem.png", "price": 2},
        {"restaurant_id": 2, "name": "Cơm tấm bì chả", "description": "Bì heo thái sợi dai giòn, chả trứng thơm béo", "image": "foods/com_tam_bi_cha.png", "price": 8},
        {"restaurant_id": 2, "name": "Chả cá chiên", "description": "Chả cá thơm lừng, chiên giòn rụm, ăn kèm mắm ngọt", "image": "foods/cha_ca_chien.png", "price": 8},
        {"restaurant_id": 2, "name": "Cơm tấm gà nướng mật ong", "description": "Gà nướng vàng óng, thơm vị mật ong, hòa quyện với cơm tấm.", "image": "foods/com_tam_ga_nuong_mat_ong.png", "price": 12},
        {"restaurant_id": 2, "name": "Canh chua cá lóc", "description": "Canh chua ngọt mát, cá lóc tươi ngon, ăn kèm cơm tấm", "image": "foods/canh_chua_ca_loc.png", "price": 8},

        #Quán Bún Bò Huế O Xuân
        {"restaurant_id": 3, "name": "Bún bò Huế giò heo", "description": "Nước dùng cay nhẹ, giò heo béo ngậy, thịt bò mềm thơm", "image": "foods/bun_bo_hue_gio_heo.png", "price": 9},
        {"restaurant_id": 3, "name": "Bánh bèo chén", "description": "Bánh bèo mềm mịn, phủ tôm cháy, mỡ hành, nước mắm ngọt", "image": "foods/banh_beo_chen.png", "price": 9},
        {"restaurant_id": 3, "name": "Chả bò hấp", "description": "Chả bò Huế thơm dai, dùng kèm rau sống", "image": "foods/cha_bo_hap.png", "price": 5},
        {"restaurant_id": 3, "name": "Nem lụi Huế", "description": "Nem lụi nướng trên than hoa, chấm kèm nước lèo đậm đà", "image": "foods/nem_lui_hue.png", "price": 7},
        {"restaurant_id": 3, "name": "Bún hến xào", "description": "Hến xào đậm vị, ăn kèm bún, rau sống và đậu phộng", "image": "foods/bun_hen_xao.png", "price": 8},
        {"restaurant_id": 3, "name": "Chè bắp Huế", "description": "Chè bắp ngọt dịu, thơm mùi lá dứa và nước cốt dừa", "image": "foods/che_bap_hue.png", "price": 6},
        {"restaurant_id": 3, "name": "Bánh lọc trần", "description": "Bánh trong suốt, nhân tôm thịt, chấm nước mắm cay ngọt", "image": "foods/banh_loc_tran.png", "price": 12},

        #Nhà hàng Phố Biển
        {"restaurant_id": 4, "name": "Cua rang me", "description": "Cua biển sốt me, thịt cua thấm vị chua ngọt hấp dẫn", "image": "foods/cua_rang_me.png", "price": 8},
        {"restaurant_id": 4, "name": "Cá nướng giấy bạc", "description": "Cá tươi giữ trọn vị ngọt, thêm hành và gia vị", "image": "foods/ca_nuong_giay_bac.png", "price": 10},
        {"restaurant_id": 4, "name": "Ghẹ hấp bia", "description": "Ghẹ tươi hấp bia thơm nồng, thịt chắc ngọt", "image": "foods/ghe_hap_bia.png", "price": 11},
        {"restaurant_id": 4, "name": "Tôm hùm nướng phô mai", "description": "Tôm hùm nướng vàng, phủ phô mai béo ngậy", "image": "foods/tom_hum_nuong_pho_mai.png", "price": 12},
        {"restaurant_id": 4, "name": "Mực xào sa tế", "description": "Mực tươi giòn, xào với sa tế cay thơm", "image": "foods/muc_xao_sa_te.png", "price": 12},
        {"restaurant_id": 4, "name": "Canh chua cá bớp", "description": "Canh chua thanh mát, cá bớp béo ngọt, rau thơm tươi ngon", "image": "restaurants/canh_chua_ca_bop.png", "price": 8},
        {"restaurant_id": 4, "name": "Hàu nướng mỡ hành", "description": "Hàu nướng vừa chín, mỡ hành và đậu phộng rắc trên", "image": "foods/hau_nuong_mo_hanh.png", "price": 9},

        #Nhà hàng Hội An
        {"restaurant_id": 5, "name": "Bánh bao Hội An", "description": "Bánh bao nhân thịt hấp mềm mịn, thơm vị cổ truyền", "image": "foods/banh_bao_hoi_an.png", "price": 7},
        {"restaurant_id": 5, "name": "Mì Quảng gà", "description": "Mì dai ngon, ăn cùng gà xé, đậu phộng và rau sống", "image": "foods/mi_quang_ga.png", "price": 7},
        {"restaurant_id": 5, "name": "Hoành thánh chiên", "description": "Hoành thánh giòn rụm, nhân thịt đậm đà, chấm nước sốt chua ngọt", "image": "foods/Hoanh_thanh_chien.png", "price": 10},
        {"restaurant_id": 5, "name": "Cao lầu Hội An", "description": "Cao lầu đặc trưng với sợi mì giòn dai, thịt xíu, rau thơm", "image": "foods/cao_lau_hoi_an.png", "price": 11},
        {"restaurant_id": 5, "name": "Bánh đập hến xào", "description": "Bánh đập giòn tan, hến xào mặn ngọt", "image": "foods/banh_dap_hen_xao.png", "price": 15},
        {"restaurant_id": 5, "name": "Cơm gà Hội An", "description": "Cơm gà xé phay, ăn kèm hành phi và nước mắm pha", "image": "foods/com_ga_hoi_an.png", "price": 14},
        {"restaurant_id": 5, "name": "Chè hạt sen", "description": "Hạt sen bùi bùi, nấu với nước đường thanh mát.", "image": "foods/che_hat_sen.png", "price": 13},
    ]

    users = [
    {
      "userid": "1",
      "username": "john_doe",
      "fullname": "John Doe",
      "email": "john.doe@example.com",
      "password": "abc"
    },
    {
      "userid": "2",
      "username": "jane_smith",
      "fullname": "Jane Smith",
      "email": "jane.smith@example.com",
      "password": "abc"
    },
    {
      "userid": "3",
      "username": "alice_wonder",
      "fullname": "Alice Wonder",
      "email": "alice.wonder@example.com",
      "password": "abc"
    },
    {
      "userid": "4",
      "username": "raiju",
      "fullname": "Alexander Pall",
      "email": "raiju@example.com",
      "password": "abc"
    }
    ]
    # Populate restaurants table
    for restaurant in restaurants:
        add_restaurant(db, restaurant["name"], restaurant["description"], restaurant["image"])

    # Populate foods table
    for food in foods:
        add_food(db, food["restaurant_id"], food["name"], food["description"], food["image"], food["price"])
    
    for user in users:
        add_user(db, user["userid"], user["username"], user["fullname"], user["email"], user["password"])
if __name__ == "__main__":
    main()
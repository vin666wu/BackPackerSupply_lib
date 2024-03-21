package www.bps.test;

import www.bps.entity.VIP;

public class TestVIP {

	public static void main(String[] args) {
		VIP vip = new VIP();
		vip.setId("A223456781");
		vip.setName("林佑莉");
		vip.setPassword("123123123");
		vip.setEmail("test781@uuu.com.tw");
		vip.setGender('F');
		vip.setBirthday(2004, 2, 2);
		vip.setPhone("0987654781");
		vip.setDiscount(10);
		
//		System.out.printf("vip.id: %s\n", vip.getId());
//		System.out.printf("vip.name: %s\n", vip.getName());
//		System.out.printf("vip.email: %s\n", vip.getEmail());
//		System.out.printf("vip.gender: %s\n", vip.getGender());
//		System.out.printf("vip.birthday: %s\n", vip.getBirthday());
//		System.out.printf("vip.phone: %s\n", vip.getPhone());
//		System.out.printf("vip.address: %s\n", vip.getAddress());
//		System.out.printf("vip.subscribed: %s\n", vip.isSubscribed());
//		
//		System.out.printf("vip.discount: %s %% off 等同於台灣的%s\n", 
//									vip.getDiscount(), vip.getDiscountString());
		
		System.out.printf("vip: %s\n", vip);
	}

}


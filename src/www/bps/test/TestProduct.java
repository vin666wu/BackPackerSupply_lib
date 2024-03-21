package www.bps.test;

import www.bps.entity.Product;

public class TestProduct {

	public static void main(String[] args) {
		//Product p = new Product();
		Product p = new Product(1, "輕旅筆電包 24L 探索黑", 3280);		
		
//		p.setId(1);
//		p.setName("Java最強入門邁向頂尖高手之路：王者歸來(第二版)全彩版");
//		p.setUnitPrice(1000);
//		p.setStock(10);
		p.setPhotoUrl(
		   "https://www.bitplayinc.com/cdn/shop/files/Urban-Daypack_black_2048x2048.jpg?v=1710125163");
		//p.setReleaseDate(LocalDate.parse("2020-10-15"));
		p.setReleaseDate("2020-10-15");
		p.setCategory("Backpack");
		
//		System.out.printf("id: %s\n", p.getId());
//		System.out.printf("name: %s\n", p.getName());
//		System.out.printf("UnitPrice: %s\n", p.getUnitPrice());
//		System.out.printf("Stock: %s\n", p.getStock());
//		System.out.printf("photoUrl: %s\n", p.getPhotoUrl());
//		System.out.printf("ReleaseDate: %s\n", p.getReleaseDate());
//		System.out.printf("Description: %s\n", p.getDescription());
		
		//p=null;
		System.out.printf("p: %s\n", p);
	}

}

package www.bps.entity;

import java.time.LocalDate;

public class Product extends Object { 
	private int id;	  				//PKey, auto-increment, >0
	private String name;			//必要, unique, 內容 >=1個字元
	private double unitPrice;		//必要, 售價即為定價
	private int stock;	 			//必要
	private String photoUrl;    	//非必要	 
	private LocalDate releaseDate; 	//必要, 出版/上架日期
	private String category;	    //必要, 書籍/文具	
	private String description="";  //非必要	
	
	public Product() {
		super();
	}

	public Product(int id, String name, double unitPrice) {
		super();
		this.setId(id);
		this.setName(name);
		this.setUnitPrice(unitPrice);
	}
	
	public Product(int id, String name, double unitPrice, int stock) {
		//super();
		this(id,name,unitPrice);
		this.setStock(stock);
	}

	public int getId() {
		return id;
	}
	public void setId(int id) {
		if(id>0) {
			this.id = id;
		}else {
			//TODO: 13章拋出 XXXException
			System.err.printf("產品代號必須為>0的正整數: %s\n", id);
		}
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		if(name!=null && name.length()>0) {
			this.name = name;
		}else {
			//TODO: 13章拋出 XXXException
			System.err.printf("產品名稱至少1個字- %s\n", name);
		}
	}
	
	/**
	 * 查詢 售價(即為定價)
	 * @return
	 */
	public double getUnitPrice() {
		return unitPrice;
	}
	public void setUnitPrice(double unitPrice) {
		this.unitPrice = unitPrice;
	}
	public int getStock() {
		return stock;
	}
	public void setStock(int stock) {
		this.stock = stock;
	}
	public String getPhotoUrl() {
		return photoUrl;
	}
	public void setPhotoUrl(String photoUrl) {
		this.photoUrl = photoUrl;
	}
	public LocalDate getReleaseDate() {
		return releaseDate;
	}
	
	public void setReleaseDate(LocalDate releaseDate) {
		this.releaseDate = releaseDate;
	}
	
	public void setReleaseDate(String releaseDate) {
		LocalDate date= LocalDate.parse(releaseDate);
		this.setReleaseDate(date);
	}
	
	public String getCategory() {
		return category;
	}
	public void setCategory(String category) {
		this.category = category;
	}
	public String getDescription() {
		return description;
	}
	public void setDescription(String description) {
		this.description = description;
	}

	@Override
	public String toString() {
		return this.getClass().getSimpleName() 
				+ "[id=" + id + ", 產品名稱=" + name + ", 定價=" + unitPrice 
				+ "\n, 庫存=" + stock + ", 上架日期=" + releaseDate+ ", 分類=" + category 
				+ ",\n 圖片Url=" + photoUrl  
				+ ",\n 描述=" + description
			+ "]";
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + id;
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Product other = (Product) obj;
		if (id != other.id)
			return false;
		return true;
	}
	 
	
	
}
 

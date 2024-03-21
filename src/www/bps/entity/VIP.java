package www.bps.entity;

public class VIP extends Customer{
	private int discount=5; //1~90 % off

	public VIP() {
		super();
	}
	
	public int getDiscount() {
		return discount;
	}

	public void setDiscount(int discount) {
		if(discount>=1 && discount<=90) {
			this.discount = discount;
		}else {
			//TODO: mod13後要改
			System.err.printf("VIP折扣必須在1~90% off- %s不正確\n", discount);
		}
	}
	
	public String getDiscountString() {
		int discount = 100-this.discount;
		if(discount%10==0) {
			discount = discount/10;
		}
		return discount + "折";
	}

	@Override
	public String toString() {
		return super.toString() + 
				"\n, VIP折扣=" + discount + "% off, 即為" + getDiscountString();
			
	}
	

	
	
}
package www.bps.test;

import www.bps.entity.Customer;

public class TestCustomer {

	public static void main(String[] args) {
		Customer c = new Customer("A123456770", " Andy Lao", "test123@example.com", 'M');
		c.setEmail("test123@example.com");
		c.setPhone("0977854632");
		c.setAddress(null);
//		int age = c.getAge();		//must set birthday
		System.out.printf("c: %s\n", c);
		
		Customer c2 = c;
		c2.setId("A123123132");
		c2.setName("Mike Lin");
		System.out.printf("c.id: %s, c2.id: %s\n", c.getId(),c2.getId());
		System.out.printf("c.name: %s, c2.name: %s\n", c.getName(), c2.getName());
		System.out.printf("c: %s\n", c);
		System.out.printf("c2: %s\n", c2);
	}

}

package www.bps.entity;

import java.time.LocalDate;
import java.time.format.DateTimeParseException;

public class Customer {
	private String id;
	private String name;
	private String email;
	private String password;

	private char gender;
	private LocalDate birthday ;
	private String phone;
	private String address = new String("");
	private boolean subscribed;

	public Customer() {
		super();
	}
	public Customer(String id, String name, String password) {
		this.setId(id);
		this.setName(name);
		this.setPassword(password);
	}
	
	public Customer(String id, String name, String password, char gender) {
		this(id, name, password);
		this.setGender(gender);
	}
	
	public String getId() {
		return id;
	}

	public void setId(String id) {
		if(checkId(id)) {
			this.id = id;
		}else {
			System.err.printf("Must enter ROC ID format. 必須輸入符合ROC ID身份證號- %s\n", id);;
		}
	}

	public boolean checkId(String id) {
		if(id!=null && id.matches("[A-Z][1289][0-9]{8}")) {
			char firstChar = id.charAt(0);
			int e1 = 0;
			switch(firstChar) {
				case 'B':case 'N':case 'Z':
					e1 = 0;break;
				case 'A':case 'M':case 'W':
					e1 = 1;break;			
				case 'K':case 'L':case 'Y':
					e1 = 2;break;
				case 'J':case 'V':case 'X':
					e1 = 3;break;			
				case 'H':case 'U':
					e1 = 4;break;
				case 'G':case 'T':
					e1 = 5;break;			
				case 'F':case 'S':
					e1 = 6;break;
				case 'E':case 'R':
					e1 = 7;break;			
				case 'D':case 'O':case 'Q':
					e1 = 8;break;
				case 'C':case 'I':case 'P':
					e1 = 9;break;		
			}
			int sum = e1;
			
			for (int i=1,j=8 ; i<=9 ; i++,j--) {
				sum = sum + (id.charAt(i)-'0')*(i==9?1:j);
			}
			
			return (sum%10==0);
		}
		
		return false;
	}
	
	public String getName() {
		return name;
	}

	public void setName(String n) {
		int minLength=2;
		int maxLength=20;
		if(n!=null && (n=n.trim()).length()>=minLength && n.length()<=maxLength) {
			this.name = n;
		}else {
			System.err.printf("Must enter%d~%d characters of customer name.", minLength,maxLength,n);
		}
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		if(email!=null && email.matches("^[\\w-\\.]+@([\\w-]+\\.)+[\\w-]{2,4}$")) {
			this.email = email;
		}else {
			System.err.printf("must enter correct format email- %s\n", email);
		}
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String pwd) {
		int minLength=6;
		int maxLength=20;
		if(pwd!=null && pwd.length()>=minLength && pwd.length()<=maxLength) {
			password = pwd;
		}else {
			System.err.printf("must enter%d~%d characters password- %s\n", minLength, maxLength, pwd);
		}
	}

	public char getGender() {
		return gender;
	}

	public void setGender(char gender) {
		if(gender=='M' || gender=='F' ||gender=='O') {
			this.gender = gender;
		}else {
			System.err.printf("must select a genderM/F/O- %s is not in the selection.\n", gender);
		}
	}

	public LocalDate getBirthday() {
		return birthday;
	}

	public void setBirthday(LocalDate birthday) {
		if(birthday!=null && 
					LocalDate.now().getYear()-birthday.getYear() >=12) {
			this.birthday = birthday;
		}else {
			System.err.printf("客戶必須年滿12歲, %s不符合條件\n", birthday);
		}
	}
	
	public void setBirthday(String dateStr) {
		if(dateStr!=null) {
			dateStr = dateStr.replace('/', '-');
		}
			try {
				LocalDate date = LocalDate.parse(dateStr);
				this.setBirthday(date);
			} catch (DateTimeParseException|NullPointerException e) {
				System.err.printf("must enter customer's birthday and match iso8601 format.");
			}
	}
	
	public void setBirthday(int year, int month, int day) {
		LocalDate date = LocalDate.of(year, month, day);
		//Date date = new GregorianCalendar(year, month-1, day).getTime(); //birthday使用java.util.Date
		this.setBirthday(date);
	}	

	public int getAge() {
		return getAge(this.birthday);
	}
	
	public int getAge(LocalDate birthday) {
		int thisYear = LocalDate.now().getYear();
		int age;
		if(birthday!=null) {
			int birthYear = birthday.getYear();
			age = thisYear-birthYear;
		}else {
			System.err.println("birthday is null , can't be calculated");
			age =-1;
		}
		return age;
	}
		
	public String getPhone() {
		return phone;
	}

	public void setPhone(String phone) {
		if(phone!=null && phone.matches("\\d{10,}")) {
			this.phone = phone;
		}else {
			System.err.printf("must enter correct cell phone format- %s\n", phone);
		}
	}

	public String getAddress() {
		return address;
	}

	public void setAddress(String address) {
		if(address==null) address="";
		this.address = address.trim();
	}

	public boolean isSubscribed() {
		return subscribed;
	}

	public void setSubscribed(boolean subscribed) {
		this.subscribed = subscribed;
	}
	
	@Override
	public String toString() {
		return "Customer [id=" + id + ", name=" + name + ", email=" + email + ", password=" + password + ", gender="
				+ gender + ", birthday=" + birthday + ", phone=" + phone + ", address=" + address + ", subscribed="
				+ subscribed + "]";
	}
	
	
}

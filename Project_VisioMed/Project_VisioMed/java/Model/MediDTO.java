package Model;

import java.sql.Date;

public class MediDTO {
	
	/*
	 CREATE TABLE t_medicine
(
    h_seq           NUMBER(12, 0)    NOT NULL, 
    med_box         VARCHAR2(50)     NULL, 
    med_name        VARCHAR2(50)     NULL, 
    med_hosp        VARCHAR2(50)     NULL, 
    med_way         VARCHAR2(50)     NULL, 
    med_date        DATE             NULL, 
    med_visit       DATE             NULL, 
    med_alarm       VARCHAR2(30)     NULL,
    med_update      DATE     		 NULL,  
); 
	 */
	
	// ����� ���� 
    private int h_seq;

    // �����Թ�ȣ 
    private String med_box;

    // ���̸� 
    private String med_name;

    // ó���Ƿ��� 
    private String med_hosp;

    // ����� 
    private String med_way;

    // ó������ 
    private String med_date;

    // ����ð��˶� 
    private String med_alarm;
    
    private String user_id;
    
    
	public MediDTO() {
		super();
	}

	public MediDTO(int h_seq, String med_box, String med_name, String med_hosp, String med_way, String med_date,
			 String med_alarm, String user_id) {
		super();
		this.h_seq = h_seq;
		this.med_box = med_box;
		this.med_name = med_name;
		this.med_hosp = med_hosp;
		this.med_way = med_way;
		this.med_date = med_date;
		this.med_alarm = med_alarm;
		this.user_id = user_id;
	}

	
	public int getH_seq() {
		return h_seq;
	}

	public void setH_seq(int h_seq) {
		this.h_seq = h_seq;
	}

	public String getMed_box() {
		return med_box;
	}

	public void setMed_box(String med_box) {
		this.med_box = med_box;
	}

	public String getMed_name() {
		return med_name;
	}

	public void setMed_name(String med_name) {
		this.med_name = med_name;
	}

	public String getMed_hosp() {
		return med_hosp;
	}

	public void setMed_hosp(String med_hosp) {
		this.med_hosp = med_hosp;
	}

	public String getMed_way() {
		return med_way;
	}

	public void setMed_way(String med_way) {
		this.med_way = med_way;
	}

	public String getMed_date() {
		return med_date;
	}

	public void setMed_date(String med_date) {
		this.med_date = med_date;
	}

	public String getMed_alarm() {
		return med_alarm;
	}

	public void setMed_alarm(String med_alarm) {
		this.med_alarm = med_alarm;
	}


	public String getUser_id() {
		return user_id;
	}


	public void setUser_id(String user_id) {
		this.user_id = user_id;
	}

}

package com.example.domain;

import java.util.Date;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.sun.istack.NotNull;

@Entity
public class CotacaoArroz {

	@JsonIgnore
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;	
	
	@NotNull
	private String Safra;
	
	@JsonFormat(pattern = "dd/MM/yyyy")
	private Date Data;
	
	@NotNull
	private boolean Preço;
	
	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public String getSafra() {
		return Safra;
	}

	public void setSafra(String Safra) {
		this.Safra = Safra;
	}

	public Date getData() {
		return Data;
	}

	public void setData(Date Data) {
		this.Data = Data;
	}

	
	public boolean getPreço() {
		return Preço;
	}

	public void setPreço(boolean Preço) {
		this.Preço = Preço;
	}

	
}
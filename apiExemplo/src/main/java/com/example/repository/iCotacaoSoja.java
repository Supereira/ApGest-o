package com.example.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.example.domain.CotacaoSoja;

@Repository
public interface iCotacaoSoja extends JpaRepository<CotacaoSoja, Long>{

	CotacaoSoja getByid(Long id);
	
}
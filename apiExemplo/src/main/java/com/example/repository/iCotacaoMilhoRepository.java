package com.example.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.example.domain.CotacaoMilho;

@Repository
public interface iCotacaoMilhoRepository extends JpaRepository<CotacaoMilho, Long>{

	CotacaoMilho getByid(Long id);
	
}
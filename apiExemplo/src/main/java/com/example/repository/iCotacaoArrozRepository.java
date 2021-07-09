package com.example.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.example.domain.CotacaoArroz;

@Repository
public interface iCotacaoArrozRepository extends JpaRepository<CotacaoArroz, Long>{

	CotacaoArroz getByid(Long id);
	
}
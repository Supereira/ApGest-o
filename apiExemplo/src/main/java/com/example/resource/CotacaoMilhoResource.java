package com.example.resource;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.domain.CotacaoMilho;
import com.example.repository.iCotacaoMilhoRepository;


@RestController
@RequestMapping("/CotacaoMilho/")
public class CotacaoMilhoResource {
	
	@Autowired
	private iCotacaoMilhoRepository repository;
	
	@GetMapping
	public ResponseEntity<List<CotacaoMilho>> listCotacaoM() {	
       	return ResponseEntity.
			   status(HttpStatus.OK).
			   body( repository.findAll() );
	}
	
	@PostMapping()
	public void salvarCotacaoMilho(@RequestBody CotacaoMilho cm) {
		repository.save(cm);
	}
	
	@PutMapping()
	public void atualizarSafra() {
		
	}
	
	@DeleteMapping()
	public void excluirSafra() {
		
	}
	
	@PutMapping()
	public void atualizarData() {
		
	}
	
	@DeleteMapping()
	public void excluirData() {
		
	}
	
	@PutMapping()
	public void atualizarPreço() {
		
	}
	
	@DeleteMapping()
	public void excluirPreço() {
		
	}
}

package ru.seals.spring.App.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import ru.seals.spring.App.models.Images;

@Repository
public interface ImageRep extends JpaRepository<Images,Integer> {
}

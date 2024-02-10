package ru.seals.spring.App.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;
import ru.seals.spring.App.models.Images;
import ru.seals.spring.App.models.Person;

import java.awt.*;
import java.util.Optional;

@Repository
public interface ImageRep extends JpaRepository<Images,Integer> {
    @Query("SELECT i FROM Images i WHERE i.trashPlace.id = :pollutionPlaceId")
    Optional<Images> findByPollutionPlaceId(int pollutionPlaceId);
}

package ru.seals.spring.App.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import ru.seals.spring.App.models.TrashPlace;

import java.util.Optional;

@Repository
public interface TrashPlaceRep extends JpaRepository<TrashPlace,Integer> {
}

package ru.seals.spring.App.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
import ru.seals.spring.App.models.Person;
import ru.seals.spring.App.models.TrashPlace;
import ru.seals.spring.App.services.ImageService;
import ru.seals.spring.App.services.PersonDetailsService;
import ru.seals.spring.App.services.PlaceProblemService;
import ru.seals.spring.App.services.RegionService;
import ru.seals.spring.App.util.ImageToByte;

import javax.servlet.http.HttpServletRequest;
import javax.validation.Valid;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.LocalDateTime;

@Controller
@RequestMapping("/problem")
public class PlaceProblemController {

    private final PersonDetailsService personDetailsService;
    private final RegionService regionService;
    private final PlaceProblemService placeProblemService;

    private final ImageToByte imageToByte;

    private final ImageService imageService;

    @Autowired
    public PlaceProblemController(PersonDetailsService personDetailsService, RegionService regionService, PlaceProblemService placeProblemService, ImageToByte imageToByte, ImageService imageService) {
        this.personDetailsService = personDetailsService;
        this.regionService = regionService;
        this.placeProblemService = placeProblemService;
        this.imageToByte = imageToByte;
        this.imageService = imageService;
    }

    @GetMapping("/add")
    public String addProblem(@ModelAttribute("problem") TrashPlace trashPlace, Model model) {
        model.addAttribute("regions",regionService.findAll());
        return "problems/addProblem";
    }

    @PostMapping("/add")
    public String doProblem(@ModelAttribute("problem") @Valid TrashPlace trashPlace, @RequestParam("latitude") double latitude, @RequestParam("longitude") double longitude, @RequestParam("region")int region,
                            @RequestParam("photo") MultipartFile photo, HttpServletRequest request) throws IOException {
        Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
        Person person = personDetailsService.loadPersonByLogin(authentication.getName());
        trashPlace.setRegion(regionService.findOne(region));
        trashPlace.setPerson(person);
        trashPlace.setDate(LocalDateTime.now());
        trashPlace.setCoordinates(latitude + " " + longitude);
        trashPlace.setProblemStatus("На рассмотрении");
        placeProblemService.save(trashPlace);
        try {
            // Определяем путь, куда будем сохранять файл
            String uploadsDir = "/";
            String realPathtoUploads =  request.getServletContext().getRealPath(uploadsDir);
            if (!Files.exists(Paths.get(realPathtoUploads))) {
                Files.createDirectories(Paths.get(realPathtoUploads));
            }

            // Получаем путь для сохранения файла
            String filename = photo.getOriginalFilename();
            String filepath = Paths.get(realPathtoUploads, filename).toString();

            // Сохраняем фото
            byte[] bytes = photo.getBytes();
            Path path = Paths.get(filepath);
            Files.write(path, bytes);
            System.out.println("Фото сохранено" + filepath);

            imageToByte.convertImageToBytesAndSave(filepath,trashPlace);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return "redirect:/hello";
    }

    @GetMapping("/{id}")
    public String view(@PathVariable("id") int id,Model model) {
        model.addAttribute("problem",placeProblemService.findOne(id));
        System.out.println(placeProblemService.findOne(id).getTrashPlaces());
        return "problems/view";
    }

}

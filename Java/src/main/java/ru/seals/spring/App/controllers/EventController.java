package ru.seals.spring.App.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import ru.seals.spring.App.models.CleaningDay;
import ru.seals.spring.App.services.CleaningDayService;
import ru.seals.spring.App.services.PlaceProblemService;

import javax.validation.Valid;
import java.time.LocalDateTime;

@Controller
@RequestMapping("/event")
public class EventController {

    private final PlaceProblemService placeProblemService;
    private final CleaningDayService cleaningDayService;

    @Autowired
    public EventController(PlaceProblemService placeProblemService, CleaningDayService cleaningDayService) {
        this.placeProblemService = placeProblemService;
        this.cleaningDayService = cleaningDayService;
    }

    @GetMapping("/addEvent")
    public String addEvent(@ModelAttribute("event") CleaningDay cleaningDay, Model model) {
        model.addAttribute("problems",placeProblemService.findAll());
        return "event/addEvent";
    }

    @PostMapping("/addEvent")
    public String doEvent(@ModelAttribute("event") @Valid CleaningDay cleaningDay,@RequestParam("problem")int problem) {
        cleaningDay.setTrashPlace(placeProblemService.findOne(problem));
        cleaningDayService.save(cleaningDay);
        return "redirect:/hello";
    }

    @GetMapping("/viewEvent")
    public String viewEvent(Model model) {
        model.addAttribute("events",cleaningDayService.findAll());
        return "event/viewEvent";
    }

    @GetMapping("/{id}")
    public String goEvent(@PathVariable("id") int id,Model model) {
        model.addAttribute("event",cleaningDayService.findOne(id));
        CleaningDay cleaningDay = cleaningDayService.findOne(id);
        int count = cleaningDay.getCountPeople();
        cleaningDay.setCountPeople(++count);
        cleaningDayService.save(cleaningDay);
        return "event/success";
    }
}

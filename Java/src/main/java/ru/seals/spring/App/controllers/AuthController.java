package ru.seals.spring.App.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import ru.seals.spring.App.models.Person;
import ru.seals.spring.App.services.RegistrationService;
import ru.seals.spring.App.util.PersonValidator;
import ru.seals.spring.App.util.UserStatus;

import javax.validation.Valid;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

@Controller
@RequestMapping("/auth")
public class AuthController {

    private final PersonValidator personValidator;
    private final RegistrationService registrationService;

    @Autowired
    public AuthController(PersonValidator personValidator, RegistrationService registrationService) {
        this.personValidator = personValidator;
        this.registrationService = registrationService;
    }

    @GetMapping("/login")
    public String loginPage() {
        return "auth/login";
    }

    @GetMapping("/registration")
    public String registrationPage(@ModelAttribute("person") Person person, Model model) {
        // Получаем массив значений перечисления UserStatus
        UserStatus[] statuses = UserStatus.values();
        // Преобразуем массив в список строк с помощью стримов
        List<String> statusList = Arrays.stream(statuses)
                .map(Enum::name)
                .map(status -> status.replace("_", " "))
                .toList(); // Собираем результаты в список


        model.addAttribute("statusList",statusList);
        return "auth/registration";
    }

    @PostMapping("/registration")
    public String doRegistration(@ModelAttribute("person") @Valid Person person,
                                 BindingResult bindingResult) {

        personValidator.validate(person,bindingResult);

        if(bindingResult.hasErrors())
            return "/auth/registration";

        registrationService.register(person);

        return "redirect:/auth/login";
    }
}

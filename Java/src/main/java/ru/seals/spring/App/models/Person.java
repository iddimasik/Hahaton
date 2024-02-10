package ru.seals.spring.App.models;

import ru.seals.spring.App.util.UserStatus;

import javax.persistence.*;
import javax.validation.constraints.Email;
import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.Pattern;
import javax.validation.constraints.Size;

@Entity
@Table(name = "users")
public class Person {

    @Id
    @Column(name = "id")
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @Column(name = "login")
    @NotEmpty(message = "Логин не должен быть пустым")
    @Size(min = 2, max = 100, message = "Логин должен быть от 2 до 100 символов длинной")
    private String login;

    @Column(name = "first_name")
    @NotEmpty(message = "Имя не должно быть пустым")
    @Size(min = 2, max = 100, message = "Имя должно быть от 2 до 100 символов длинной")
    private String firstName;

    @Column(name = "last_name")
    @NotEmpty(message = "Фамилия не должна быть пустым")
    @Size(min = 2, max = 100, message = "Фамилия должна быть от 2 до 100 символов длинной")
    private String lastName;

    @Column(name = "email")
    @Email(message = "Некорректный адрес электронной почты")
    private String email;

    @Column(name = "password")
    @Size(min = 8, max = 100, message = "Пароль должен быть от 8 до 100 символов длинной")
    private String password;

    @Column(name = "user_status")
    private String userStatus;

    @Column(name = "phone_number")
    @Pattern(regexp="\\+?[0-9]+", message="Некорректный номер телефона")
    private String phoneNumber;

    @Column(name = "role")
    private String role;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getUserStatus() {
        return userStatus;
    }

    public void setUserStatus(String userStatus) {
        this.userStatus = userStatus;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }
}

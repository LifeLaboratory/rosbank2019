package ru.lifelaboratory.rosbank.entity;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

/**
 * Сущность для авторизации
 * @author Boris Bockarev <Boris-Bochkaryov@yandex.ru>
 */
@NoArgsConstructor
@AllArgsConstructor
@Setter
@Getter
public class Auth {

    private String login;
    private String password;

}

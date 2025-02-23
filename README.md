# Django Furniture Shop

## Описание

Django Furniture Shop — это полноценное веб-приложение для онлайн-магазина мебели, разработанное с использованием Django. Проект предлагает пользователям удобный интерфейс для просмотра, добавления в корзину и покупки различных товаров. Реализованы функции аутентификации пользователей, регистрация, текстовый поиск, фильтрация и пагинация.

---

## Стек технологий

- **Django** — основной фреймворк для разработки веб-приложений.
  
- **Djoser** — библиотека для упрощения аутентификации пользователей.
  
- **PostgreSQL** — для хранения данных.

---

## Основные функции

1. **Аутентификация и регистрация**:
   - Пользователи могут зарегистрироваться и войти в систему.
   - Реализована система восстановления пароля.

2. **Пагинация**:
   - Список товаров разбит на страницы, что позволяет пользователям легко просматривать ассортимент.

3. **Фильтрация**:
   - Пользователи могут фильтровать товары по категориям, цене, рейтингу и другим параметрам.

4. **Полноценный текстовый поиск**:
   - Пользователи могут искать товары по названию и описанию, используя мощный механизм поиска.

5. **Корзина покупок**:
   - Пользователи могут добавлять товары в корзину, изменять количество и удалять товары.

6. **История заказов**:
   - Пользователи могут просматривать свою историю покупок и статусы заказов.

7. **Адаптивный дизайн**:
   - Интерфейс приложения адаптирован для различных устройств — ПК, планшетов и мобильных телефонов.

---

## Спецификация API

### Аутентификация

- **Получение токена:**
  
  - **POST /api/v1/token/**
  
  - Тело запроса:
    
    json
    {
      "username": "your_username",
      "password": "your_password"
    }
    
- **Регистрация пользователя:**
  
  - **POST /api/v1/register/**
  
  - Тело запроса:
    
    json
    {
      "username": "your_username",
      "email": "your_email@example.com",
      "password": "your_password"
    }
    
### Работа с товарами

- **Получение списка товаров с пагинацией и фильтрацией:**
  
  - **GET /api/v1/products/?page=1&category=category_slug&price_min=100&price_max=500**

- **Получение деталей товара:**
  
  - **GET /api/v1/products/<slug:product_slug>/**

- **Создание нового товара:**
  
  - **POST /api/v1/products/**
  
  - Тело запроса:
    
    json
    {
      "name": "Название товара",
      "description": "Описание товара",
      "price": "Цена",
      "category": "Категория"
    }
    
### Поиск товаров

- **Поиск товаров по ключевым словам:**
  
  - **GET /api/v1/products/search/?query=search_term**

### Работа с корзиной

- **Добавление товара в корзину:**
  
  - **POST /api/v1/cart/add/**
  
  - Тело запроса:
    
    json
    {
      "product_id": "ID товара",
      "quantity": "Количество"
    }
    
### Оформление заказа

- **Создание нового заказа:**
  
  - **POST /api/v1/orders/create/**
  
  - Тело запроса:
    
    json
    {
      "address": "Адрес доставки",
      "payment_method": "Способ оплаты"
    }
    
---

## Чистая архитектура

Проект реализован с использованием принципов чистой архитектуры, что позволяет легко поддерживать и расширять приложение. Каждый компонент изолирован, что обеспечивает высокую степень тестируемости и гибкости. Логика приложения разделена на слои, включая:

- Слой представления (views)
- Слой бизнес-логики (services)
- Слой доступа к данным (repositories)

---

## Значительные функции и фичи

1. **Интуитивно понятный интерфейс**: Пользователи могут легко находить и просматривать товары благодаря простому и понятному дизайну.

2. **Управление пользователями**: Реализована полноценная система аутентификации и регистрации пользователей с помощью Djoser.

3. **Корзина покупок**: Пользователи могут добавлять товары в корзину, изменять количество и удалять товары по желанию.4. **История заказов**: После оформления заказа пользователи могут просматривать историю своих покупок.

5. **RESTful API**: Все функции доступны через хорошо документированный RESTful API, что упрощает интеграцию с другими приложениями и фронтенд-клиентами.

6. **Безопасность данных**: Использование токенов для аутентификации обеспечивает безопасность пользовательских данных.

7. **Фильтрация и пагинация**: Удобные инструменты для навигации по большому количеству товаров.

8. **Текстовый поиск**: Мгновенный поиск по товарам с использованием.

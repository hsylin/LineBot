# LineBot

## Introduction
Due to the ongoing underwater pandemic, Mr. Krabs has decided to launch an online service to increase customer traffic. By utilizing online reservations, the restaurant aims to avoid government fines for violating pandemic restrictions.

## Environment
- Ubuntu 20.04
- Python 3.8.10

## Instructions

1. Install `pipenv`
    ```bash
    pip3 install pipenv
    ```

2. Install the required packages
    ```bash
    pipenv install --three
    # If pygraphviz installation fails, try the following:
    sudo apt-get install graphviz graphviz-dev
    ```

3. Create a `.env` file from `.env.sample`, and fill in the following information:
    - **Line**
        - `LINE_CHANNEL_SECRET`
        - `LINE_CHANNEL_ACCESS_TOKEN`

4. Install `ngrok`
    ```bash
    sudo snap install ngrok
    ```

5. Run `ngrok` to deploy the Line Chat Bot locally:
    ```bash
    ngrok http 8000
    ```

6. Execute `app.py`
    ```bash
    python3 app.py
    ```

## Features
- Welcome message when added as a friend
- Reservation:
    - Number of people
    - Reservation time
- View menu
- View restaurant location
- Meet the restaurant staff
- Customer survey

## Demonstration

### Welcome Message
![Welcome Message](https://img.onl/DqAJfe)

### Reservation
![Reservation](https://img.onl/G7Yol)

### View Menu
![View Menu](https://img.onl/C73X5L)

### View Restaurant Location
![View Location](https://img.onl/mEPP2x)

### Meet the Staff
![Meet Staff](https://img.onl/Ce519F)

### Customer Survey
![Survey](https://img.onl/wBo1S5)

## Finite State Machine (FSM)
![FSM](https://img.onl/zQ4JtS)

### State Descriptions
- **user**: Enter "Krabby Patty" to start using the online service
- **choose**: Select the desired service
- **reserve_people**: Enter the number of people for the reservation
- **reserve_time**: Select the reservation time
- **reserve_result**: View the reservation details
- **menu**: View the restaurant menu
- **location**: View the restaurant location
- **employee**: Meet the restaurant staff

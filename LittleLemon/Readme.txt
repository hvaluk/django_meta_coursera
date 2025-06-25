Little Lemon Restaurant API

✅ Testable API endpoints:

1. /test/                       - Simple test view (returns "Hello, world!")
2. /menu/                      - List and create menu items (GET/POST)
3. /menu/<int:pk>/             - Retrieve, update, or delete a menu item (GET/PUT/DELETE)
4. /bookings/                  - Get bookings for a date or create a new booking (GET/POST)
5. /reservations/              - View bookings via frontend
6. /book/                      - Make a booking via form
7. /message/                   - Protected API view (requires token auth)
8. /api-token-auth/            - Get authentication token (POST with username & password)
9. /tables/                    - BookingViewSet (view, add, edit bookings via DRF viewset)
10. /auth/users/               - Djoser: register new users
11. /auth/token/login/         - Djoser: login and get token
12. /auth/token/logout/        - Djoser: logout and remove token

📌 Note:
- Some endpoints require authentication (`TokenAuthentication`).
- Use `/api-token-auth/` or `/auth/token/login/` to obtain a token.
- Use the token in the header: `Authorization: Token <your_token>`.
import random
from faker import Faker
from models import Booking, Status

fake = Faker('en_IN')  # Create a Faker instance for Indian data

def generate_random_booking_and_save(n):
    # Generate random data
    for _ in range(n):
        user_name = fake.name()
        facilities = ["Stadium", "Gymnasium", "Tennis Court", "Swimming Pool"]
        facility_name = random.choice(facilities)
        start_date = datetime.now() + timedelta(days=random.randint(1, 30))
        start_time = datetime.now().replace(hour=random.randint(8, 18), minute=random.randint(0, 59))
        end_date = start_date + timedelta(days=random.randint(0, 7))
        end_time = start_time + timedelta(hours=random.randint(1, 4))
        start_hour = random.randint(8, 18)
        end_hour = start_hour + random.randint(1, 4)
        purposes = ["Training", "Match", "Practice", "Fitness Session"]
        purpose = random.choice(purposes)
        statuses = ["Pending", "Approved", "Cancelled"]
        status = random.choice(statuses)

        # Get a random Facility Manager user (assuming User model has a role attribute)
        facility_manager = User.objects.filter(role__role='FacilityManager').order_by('?').first()

        # Create and save Facility object
        facility = Facility.objects.create(
            name=facility_name,
            address=fake.address(),
            phone=fake.phone_number(),
            email=fake.email(),
            website=fake.url() if random.choice([True, False]) else None,
            location_url=fake.url() if random.choice([True, False]) else None,
            facility_manager=facility_manager
        )
        
        # Assuming Facility has a relation to bookings, you can link it accordingly
        booking = facility.booking_set.create(
            user_name=user_name,
            start_date=start_date.date(),
            start_time=start_time.time(),
            end_date=end_date.date(),
            end_time=end_time.time(),
            start_hour=start_hour,
            end_hour=end_hour,
            purpose=purpose,
            status=status
        )

        # Return the created booking object
        return booking


# Example usage:
n = int(input("Enter number of bookings to generate: "))
created_booking = generate_random_booking_and_save(n)
print("Booking created and saved:", created_booking)


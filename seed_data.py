import os
import django
from django.utils.text import slugify

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aldafnia_config.settings')
django.setup()

from products.models import Category, Product, Specification
from projects.models import Project
from media_center.models import NewsArticle, Certificate

def seed_data():
    print("Seeding data...")

    # 1. Products
    c1, _ = Category.objects.get_or_create(
        name="أنابيب HDPE (ضغط عالٍ)",
        slug="hdpe-pipes",
        defaults={"description": "أنابيب البولي إيثيلين عالي الكثافة PE100 لمشاريع المياه والغاز."}
    )
    c1.name_en = "HDPE Pipes (High Pressure)"
    c1.description_en = "High Density Polyethylene PE100 pipes for water and gas projects."
    c1.save()

    c2, _ = Category.objects.get_or_create(
        name="أنابيب الري بالتنقيط",
        slug="drip-irrigation",
        defaults={"description": "حلول متقدمة للري الزراعي بكفاءة عالية في استهلاك المياه."}
    )
    c2.name_en = "Drip Irrigation Pipes"
    c2.description_en = "Advanced solutions for agricultural irrigation with high water efficiency."
    c2.save()

    p1, _ = Product.objects.get_or_create(
        category=c1,
        slug="hdpe-pe100-water",
        defaults={
            "name": "أنابيب HDPE PE100 للمياه",
            "description": "أنابيب مخصصة لنقل مياه الشرب بضغوط تتراوح من 6 إلى 25 بار.",
            "features": "مقاومة عالية للتآكل\nمرونة فائقة\nعمر افتراضي يزيد عن 50 عاماً\nسهولة التركيب"
        }
    )
    p1.name_en = "HDPE PE100 Water Pipes"
    p1.description_en = "Pipes designed for drinking water transport with pressures from 6 to 25 bar."
    p1.features_en = "High corrosion resistance\nSuperior flexibility\nLifespan over 50 years\nEase of installation"
    p1.save()

    Specification.objects.get_or_create(product=p1, key="المادة الخام", value="PE100")
    Specification.objects.get_or_create(product=p1, key="الأقطار المتوفرة", value="20mm - 1200mm")
    Specification.objects.get_or_create(product=p1, key="درجة الضغط", value="PN6 - PN25")

    # 2. Projects
    Project.objects.get_or_create(
        slug="misrata-water-network",
        defaults={
            "title": "مشروع شبكة مياه مصراتة",
            "description": "توريد أنابيب HDPE لمشروع توسعة شبكة مياه الشرب في مدينة مصراتة.",
            "location": "مصراتة، ليبيا",
            "year": 2022
        }
    )

    # 3. Media Center
    NewsArticle.objects.get_or_create(
        slug="iso-certification-2023",
        defaults={
            "title": "حصول المصنع على شهادات الأيزو الدولية",
            "content": "نجح مصنع الدافنية في تجديد اعتمادات الأيزو 9001 و 14001 و 45001 لعام 2023."
        }
    )

    Certificate.objects.get_or_create(
        title="ISO 9001:2015",
        defaults={"description": "شهادة اعتماد نظام إدارة الجودة الدولية."}
    )

    print("Data seeded successfully!")

if __name__ == "__main__":
    seed_data()

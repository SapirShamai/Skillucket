# Generated by Django 4.2.4 on 2023-09-06 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skillucketApp', '0003_skill_userskill_bucketskill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('language', 'Language'), ('music', 'Music'), ('general_life_skills', 'General Life Skills'), ('hobbies_and_crafts', 'Hobbies and Crafts'), ('visual_arts', 'Visual Arts'), ('programming', 'Programming'), ('crime_and_exploitation', 'Crime and Exploitation')], max_length=100)),
                ('description', models.TextField(default='No description available')),
            ],
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(choices=[('language_english', 'English'), ('language_german', 'German'), ('language_french', 'French'), ('language_chinese', 'Chinese'), ('language_spanish', 'Spanish'), ('language_portuguese', 'Portuguese'), ('language_hindi', 'Hindi'), ('language_arabic', 'Arabic'), ('language_russian', 'Russian'), ('language_japanese', 'Japanese'), ('music_opera_singing', 'Opera singing'), ('music_metal_singing', 'Metal singing'), ('music_acoustic_guitar', 'Acoustic guitar'), ('music_trombone', 'Trombone'), ('music_piano', 'Piano'), ('music_music_theory', 'Music theory'), ('music_violin', 'Violin'), ('music_flute', 'Flute'), ('music_drums', 'Drums'), ('music_electronic_music', 'Electronic music'), ('general_life_skills_simple_cooking', 'Simple cooking'), ('general_life_skills_baking_bread_and_pastries', 'Baking bread and pastries'), ('general_life_skills_cleaning', 'Cleaning'), ('general_life_skills_gardening_and_caring_for_plants', 'Gardening and caring for plants'), ('general_life_skills_space_organizing', 'Space organizing'), ('general_life_skills_time_management', 'Time management'), ('general_life_skills_household_repairs', 'Household repairs'), ('general_life_skills_stress_management', 'Stress management'), ('general_life_skills_personal_finances', 'Personal finances'), ('general_life_skills_caring_for_clothes_and_textiles', 'Caring for clothes and textiles'), ('general_life_skills_conflict_resolution', 'Conflict resolution'), ('hobbies_and_crafts_crochet', 'Crochet'), ('hobbies_and_crafts_sewing', 'Sewing'), ('hobbies_and_crafts_collages', 'Collages'), ('hobbies_and_crafts_fishing', 'Fishing'), ('hobbies_and_crafts_woodwork', 'Woodwork'), ('hobbies_and_crafts_pottery', 'Pottery'), ('hobbies_and_crafts_clay_sculpting', 'Clay sculpting'), ('hobbies_and_crafts_mandalas', 'Mandalas'), ('hobbies_and_crafts_candle_making', 'Candle making'), ('hobbies_and_crafts_soap_making', 'Soap making'), ('hobbies_and_crafts_dancing', 'Dancing'), ('visual_arts_watercolor', 'Watercolor'), ('visual_arts_photoshop', 'Photoshop'), ('visual_arts_illustrator', 'Illustrator'), ('visual_arts_gesture_drawings', 'Gesture drawings'), ('visual_arts_sketching', 'Sketching'), ('visual_arts_graffiti', 'Graffiti'), ('visual_arts_acrylic_painting', 'Acrylic painting'), ('visual_arts_acrylic_pouring', 'Acrylic pouring'), ('visual_arts_oil_painting', 'Oil painting'), ('visual_arts_creating_comics', 'Creating comics'), ('programming_python', 'Python'), ('programming_c_sharp', 'C#'), ('programming_c_plus_plus', 'C++'), ('programming_c', 'C'), ('programming_java', 'Java'), ('programming_javascript', 'Javascript'), ('programming_groovy', 'Groovy'), ('programming_assembler', 'Assembler'), ('programming_cobol', 'Cobol'), ('programming_algorithms', 'Algorithms'), ('crime_and_exploitation_phishing', 'Phishing'), ('crime_and_exploitation_pickpocketing', 'Pickpocketing'), ('crime_and_exploitation_unethical_hacking', 'Unethical hacking'), ('crime_and_exploitation_manipulation', 'Manipulation'), ('crime_and_exploitation_social_engineering', 'Social Engineering'), ('crime_and_exploitation_scams', 'Scams'), ('crime_and_exploitation_blackmail', 'Blackmail'), ('crime_and_exploitation_creating_viruses', 'Creating viruses')], max_length=255),
        ),
        migrations.AlterField(
            model_name='skill',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skillucketApp.category'),
        ),
    ]

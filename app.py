from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from flask_bcrypt import Bcrypt
import sqlite3

app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    major = db.Column(db.String(20), nullable=False)
    nation = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(500), nullable=False)

class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    city = StringField(validators=[
                           InputRequired(), Length(min=3, max=20)], render_kw={"placeholder": "City"})

    major = SelectField(choices=[('GENERAL AGRICULTURE', 'GENERAL AGRICULTURE'),
('AGRICULTURE PRODUCTION AND MANAGEMENT', 'AGRICULTURE PRODUCTION AND MANAGEMENT'),
('AGRICULTURAL ECONOMICS', 'AGRICULTURAL ECONOMICS'),
('ANIMAL SCIENCES', 'ANIMAL SCIENCES'),
('FOOD SCIENCE', 'FOOD SCIENCE'),
('PLANT SCIENCE AND AGRONOMY', 'PLANT SCIENCE AND AGRONOMY'),
('SOIL SCIENCE', 'SOIL SCIENCE'),
('MISCELLANEOUS AGRICULTURE', 'MISCELLANEOUS AGRICULTURE'),
('FORESTRY', 'FORESTRY'),
('NATURAL RESOURCES MANAGEMENT', 'NATURAL RESOURCES MANAGEMENT'),
('FINE ARTS', 'FINE ARTS'),
('DRAMA AND THEATER ARTS', 'DRAMA AND THEATER ARTS'),
('MUSIC', 'MUSIC'),
('VISUAL AND PERFORMING ARTS', 'VISUAL AND PERFORMING ARTS'),
('COMMERCIAL ART AND GRAPHIC DESIGN', 'COMMERCIAL ART AND GRAPHIC DESIGN'),
('FILM VIDEO AND PHOTOGRAPHIC ARTS', 'FILM VIDEO AND PHOTOGRAPHIC ARTS'),
('STUDIO ARTS', 'STUDIO ARTS'),
('MISCELLANEOUS FINE ARTS', 'MISCELLANEOUS FINE ARTS'),
('ENVIRONMENTAL SCIENCE', 'ENVIRONMENTAL SCIENCE'),
('BIOLOGY', 'BIOLOGY'),
('BIOCHEMICAL SCIENCES', 'BIOCHEMICAL SCIENCES'),
('BOTANY', 'BOTANY'),
('MOLECULAR BIOLOGY', 'MOLECULAR BIOLOGY'),
('ECOLOGY', 'ECOLOGY'),
('GENETICS', 'GENETICS'),
('MICROBIOLOGY', 'MICROBIOLOGY'),
('PHARMACOLOGY', 'PHARMACOLOGY'),
('PHYSIOLOGY', 'PHYSIOLOGY'),
('ZOOLOGY', 'ZOOLOGY'),
('NEUROSCIENCE', 'NEUROSCIENCE'),
('MISCELLANEOUS BIOLOGY', 'MISCELLANEOUS BIOLOGY'),
('COGNITIVE SCIENCE AND BIOPSYCHOLOGY', 'COGNITIVE SCIENCE AND BIOPSYCHOLOGY'),
('GENERAL BUSINESS', 'GENERAL BUSINESS'),
('ACCOUNTING', 'ACCOUNTING'),
('ACTUARIAL SCIENCE', 'ACTUARIAL SCIENCE'),
('BUSINESS MANAGEMENT AND ADMINISTRATION', 'BUSINESS MANAGEMENT AND ADMINISTRATION'),
('OPERATIONS LOGISTICS AND E-COMMERCE', 'OPERATIONS LOGISTICS AND E-COMMERCE'),
('BUSINESS ECONOMICS', 'BUSINESS ECONOMICS'),
('MARKETING AND MARKETING RESEARCH', 'MARKETING AND MARKETING RESEARCH'),
('FINANCE', 'FINANCE'),
('HUMAN RESOURCES AND PERSONNEL MANAGEMENT', 'HUMAN RESOURCES AND PERSONNEL MANAGEMENT'),
('INTERNATIONAL BUSINESS', 'INTERNATIONAL BUSINESS'),
('HOSPITALITY MANAGEMENT', 'HOSPITALITY MANAGEMENT'),
('MANAGEMENT INFORMATION SYSTEMS AND STATISTICS', 'MANAGEMENT INFORMATION SYSTEMS AND STATISTICS'),
('MISCELLANEOUS BUSINESS & MEDICAL ADMINISTRATION', 'MISCELLANEOUS BUSINESS & MEDICAL ADMINISTRATION'),
('COMMUNICATIONS', 'COMMUNICATIONS'),
('JOURNALISM', 'JOURNALISM'),
('MASS MEDIA', 'MASS MEDIA'),
('ADVERTISING AND PUBLIC RELATIONS', 'ADVERTISING AND PUBLIC RELATIONS'),
('COMMUNICATION TECHNOLOGIES', 'COMMUNICATION TECHNOLOGIES'),
('COMPUTER AND INFORMATION SYSTEMS', 'COMPUTER AND INFORMATION SYSTEMS'),
('COMPUTER PROGRAMMING AND DATA PROCESSING', 'COMPUTER PROGRAMMING AND DATA PROCESSING'),
('COMPUTER SCIENCE', 'COMPUTER SCIENCE'),
('INFORMATION SCIENCES', 'INFORMATION SCIENCES'),
('COMPUTER ADMINISTRATION MANAGEMENT AND SECURITY', 'COMPUTER ADMINISTRATION MANAGEMENT AND SECURITY'),
('COMPUTER NETWORKING AND TELECOMMUNICATIONS', 'COMPUTER NETWORKING AND TELECOMMUNICATIONS'),
('MATHEMATICS', 'MATHEMATICS'),
('APPLIED MATHEMATICS', 'APPLIED MATHEMATICS'),
('STATISTICS AND DECISION SCIENCE', 'STATISTICS AND DECISION SCIENCE'),
('MATHEMATICS AND COMPUTER SCIENCE', 'MATHEMATICS AND COMPUTER SCIENCE'),
('GENERAL EDUCATION', 'GENERAL EDUCATION'),
('EDUCATIONAL ADMINISTRATION AND SUPERVISION', 'EDUCATIONAL ADMINISTRATION AND SUPERVISION'),
('SCHOOL STUDENT COUNSELING', 'SCHOOL STUDENT COUNSELING'),
('ELEMENTARY EDUCATION', 'ELEMENTARY EDUCATION'),
('MATHEMATICS TEACHER EDUCATION', 'MATHEMATICS TEACHER EDUCATION'),
('PHYSICAL AND HEALTH EDUCATION TEACHING', 'PHYSICAL AND HEALTH EDUCATION TEACHING'),
('EARLY CHILDHOOD EDUCATION', 'EARLY CHILDHOOD EDUCATION'),
('SCIENCE AND COMPUTER TEACHER EDUCATION', 'SCIENCE AND COMPUTER TEACHER EDUCATION'),
('SECONDARY TEACHER EDUCATION', 'SECONDARY TEACHER EDUCATION'),
('SPECIAL NEEDS EDUCATION', 'SPECIAL NEEDS EDUCATION'),
('SOCIAL SCIENCE OR HISTORY TEACHER EDUCATION', 'SOCIAL SCIENCE OR HISTORY TEACHER EDUCATION'),
('TEACHER EDUCATION: MULTIPLE LEVELS', 'TEACHER EDUCATION: MULTIPLE LEVELS'),
('LANGUAGE AND DRAMA EDUCATION', 'LANGUAGE AND DRAMA EDUCATION'),
('ART AND MUSIC EDUCATION', 'ART AND MUSIC EDUCATION'),
('MISCELLANEOUS EDUCATION', 'MISCELLANEOUS EDUCATION'),
('LIBRARY SCIENCE', 'LIBRARY SCIENCE'),
('ARCHITECTURE', 'ARCHITECTURE'),
('GENERAL ENGINEERING', 'GENERAL ENGINEERING'),
('AEROSPACE ENGINEERING', 'AEROSPACE ENGINEERING'),
('BIOLOGICAL ENGINEERING', 'BIOLOGICAL ENGINEERING'),
('ARCHITECTURAL ENGINEERING', 'ARCHITECTURAL ENGINEERING'),
('BIOMEDICAL ENGINEERING', 'BIOMEDICAL ENGINEERING'),
('CHEMICAL ENGINEERING', 'CHEMICAL ENGINEERING'),
('CIVIL ENGINEERING', 'CIVIL ENGINEERING'),
('COMPUTER ENGINEERING', 'COMPUTER ENGINEERING'),
('ELECTRICAL ENGINEERING', 'ELECTRICAL ENGINEERING'),
('ENGINEERING MECHANICS PHYSICS AND SCIENCE', 'ENGINEERING MECHANICS PHYSICS AND SCIENCE'),
('ENVIRONMENTAL ENGINEERING', 'ENVIRONMENTAL ENGINEERING'),
('GEOLOGICAL AND GEOPHYSICAL ENGINEERING', 'GEOLOGICAL AND GEOPHYSICAL ENGINEERING'),
('INDUSTRIAL AND MANUFACTURING ENGINEERING', 'INDUSTRIAL AND MANUFACTURING ENGINEERING'),
('MATERIALS ENGINEERING AND MATERIALS SCIENCE', 'MATERIALS ENGINEERING AND MATERIALS SCIENCE'),
('MECHANICAL ENGINEERING', 'MECHANICAL ENGINEERING'),
('METALLURGICAL ENGINEERING', 'METALLURGICAL ENGINEERING'),
('MINING AND MINERAL ENGINEERING', 'MINING AND MINERAL ENGINEERING'),
('NAVAL ARCHITECTURE AND MARINE ENGINEERING', 'NAVAL ARCHITECTURE AND MARINE ENGINEERING'),
('NUCLEAR ENGINEERING', 'NUCLEAR ENGINEERING'),
('PETROLEUM ENGINEERING', 'PETROLEUM ENGINEERING'),
('MISCELLANEOUS ENGINEERING', 'MISCELLANEOUS ENGINEERING'),
('ENGINEERING TECHNOLOGIES', 'ENGINEERING TECHNOLOGIES'),
('ENGINEERING AND INDUSTRIAL MANAGEMENT', 'ENGINEERING AND INDUSTRIAL MANAGEMENT'),
('ELECTRICAL ENGINEERING TECHNOLOGY', 'ELECTRICAL ENGINEERING TECHNOLOGY'),
('INDUSTRIAL PRODUCTION TECHNOLOGIES', 'INDUSTRIAL PRODUCTION TECHNOLOGIES'),
('MECHANICAL ENGINEERING RELATED TECHNOLOGIES', 'MECHANICAL ENGINEERING RELATED TECHNOLOGIES'),
('MISCELLANEOUS ENGINEERING TECHNOLOGIES', 'MISCELLANEOUS ENGINEERING TECHNOLOGIES'),
('MATERIALS SCIENCE', 'MATERIALS SCIENCE'),
('NUTRITION SCIENCES', 'NUTRITION SCIENCES'),
('GENERAL MEDICAL AND HEALTH SERVICES', 'GENERAL MEDICAL AND HEALTH SERVICES'),
('COMMUNICATION DISORDERS SCIENCES AND SERVICES', 'COMMUNICATION DISORDERS SCIENCES AND SERVICES'),
('HEALTH AND MEDICAL ADMINISTRATIVE SERVICES', 'HEALTH AND MEDICAL ADMINISTRATIVE SERVICES'),
('MEDICAL ASSISTING SERVICES', 'MEDICAL ASSISTING SERVICES'),
('MEDICAL TECHNOLOGIES TECHNICIANS', 'MEDICAL TECHNOLOGIES TECHNICIANS'),
('HEALTH AND MEDICAL PREPARATORY PROGRAMS', 'HEALTH AND MEDICAL PREPARATORY PROGRAMS'),
('NURSING', 'NURSING'),
('PHARMACY PHARMACEUTICAL SCIENCES AND ADMINISTRATION', 'PHARMACY PHARMACEUTICAL SCIENCES AND ADMINISTRATION'),
('TREATMENT THERAPY PROFESSIONS', 'TREATMENT THERAPY PROFESSIONS'),
('COMMUNITY AND PUBLIC HEALTH', 'COMMUNITY AND PUBLIC HEALTH'),
('MISCELLANEOUS HEALTH MEDICAL PROFESSIONS', 'MISCELLANEOUS HEALTH MEDICAL PROFESSIONS'),
('AREA ETHNIC AND CIVILIZATION STUDIES', 'AREA ETHNIC AND CIVILIZATION STUDIES'),
('LINGUISTICS AND COMPARATIVE LANGUAGE AND LITERATURE', 'LINGUISTICS AND COMPARATIVE LANGUAGE AND LITERATURE'),
('FRENCH GERMAN LATIN AND OTHER COMMON FOREIGN LANGUAGE STUDIES', 'FRENCH GERMAN LATIN AND OTHER COMMON FOREIGN LANGUAGE STUDIES'),
('OTHER FOREIGN LANGUAGES', 'OTHER FOREIGN LANGUAGES'),
('ENGLISH LANGUAGE AND LITERATURE', 'ENGLISH LANGUAGE AND LITERATURE'),
('COMPOSITION AND RHETORIC', 'COMPOSITION AND RHETORIC'),
('LIBERAL ARTS', 'LIBERAL ARTS'),
('HUMANITIES', 'HUMANITIES'),
('INTERCULTURAL AND INTERNATIONAL STUDIES', 'INTERCULTURAL AND INTERNATIONAL STUDIES'),
('PHILOSOPHY AND RELIGIOUS STUDIES', 'PHILOSOPHY AND RELIGIOUS STUDIES'),
('THEOLOGY AND RELIGIOUS VOCATIONS', 'THEOLOGY AND RELIGIOUS VOCATIONS'),
('ANTHROPOLOGY AND ARCHEOLOGY', 'ANTHROPOLOGY AND ARCHEOLOGY'),
('ART HISTORY AND CRITICISM', 'ART HISTORY AND CRITICISM'),
('HISTORY', 'HISTORY'),
('UNITED STATES HISTORY', 'UNITED STATES HISTORY'),
('COSMETOLOGY SERVICES AND CULINARY ARTS', 'COSMETOLOGY SERVICES AND CULINARY ARTS'),
('FAMILY AND CONSUMER SCIENCES', 'FAMILY AND CONSUMER SCIENCES'),
('MILITARY TECHNOLOGIES', 'MILITARY TECHNOLOGIES'),
('PHYSICAL FITNESS PARKS RECREATION AND LEISURE', 'PHYSICAL FITNESS PARKS RECREATION AND LEISURE'),
('CONSTRUCTION SERVICES', 'CONSTRUCTION SERVICES'),
('ELECTRICAL, MECHANICAL, AND PRECISION TECHNOLOGIES AND PRODUCTION', 'ELECTRICAL, MECHANICAL, AND PRECISION TECHNOLOGIES AND PRODUCTION'),
('TRANSPORTATION SCIENCES AND TECHNOLOGIES', 'TRANSPORTATION SCIENCES AND TECHNOLOGIES'),
('MULTI/INTERDISCIPLINARY STUDIES', 'MULTI/INTERDISCIPLINARY STUDIES'),
('COURT REPORTING', 'COURT REPORTING'),
('PRE-LAW AND LEGAL STUDIES', 'PRE-LAW AND LEGAL STUDIES'),
('CRIMINAL JUSTICE AND FIRE PROTECTION', 'CRIMINAL JUSTICE AND FIRE PROTECTION'),
('PUBLIC ADMINISTRATION', 'PUBLIC ADMINISTRATION'),
('PUBLIC POLICY', 'PUBLIC POLICY'),
('PHYSICAL SCIENCES', 'PHYSICAL SCIENCES'),
('ASTRONOMY AND ASTROPHYSICS', 'ASTRONOMY AND ASTROPHYSICS'),
('ATMOSPHERIC SCIENCES AND METEOROLOGY', 'ATMOSPHERIC SCIENCES AND METEOROLOGY'),
('CHEMISTRY', 'CHEMISTRY'),
('GEOLOGY AND EARTH SCIENCE', 'GEOLOGY AND EARTH SCIENCE'),
('GEOSCIENCES', 'GEOSCIENCES'),
('OCEANOGRAPHY', 'OCEANOGRAPHY'),
('PHYSICS', 'PHYSICS'),
('MULTI-DISCIPLINARY OR GENERAL SCIENCE', 'MULTI-DISCIPLINARY OR GENERAL SCIENCE'),
('NUCLEAR, INDUSTRIAL RADIOLOGY, AND BIOLOGICAL TECHNOLOGIES', 'NUCLEAR, INDUSTRIAL RADIOLOGY, AND BIOLOGICAL TECHNOLOGIES'),   
('PSYCHOLOGY', 'PSYCHOLOGY'),
('EDUCATIONAL PSYCHOLOGY', 'EDUCATIONAL PSYCHOLOGY'),
('CLINICAL PSYCHOLOGY', 'CLINICAL PSYCHOLOGY'),
('COUNSELING PSYCHOLOGY', 'COUNSELING PSYCHOLOGY'),
('INDUSTRIAL AND ORGANIZATIONAL PSYCHOLOGY', 'INDUSTRIAL AND ORGANIZATIONAL PSYCHOLOGY'),
('SOCIAL PSYCHOLOGY', 'SOCIAL PSYCHOLOGY'),
('MISCELLANEOUS PSYCHOLOGY', 'MISCELLANEOUS PSYCHOLOGY'),
('HUMAN SERVICES AND COMMUNITY ORGANIZATION', 'HUMAN SERVICES AND COMMUNITY ORGANIZATION'),
('SOCIAL WORK', 'SOCIAL WORK'),
('INTERDISCIPLINARY SOCIAL SCIENCES', 'INTERDISCIPLINARY SOCIAL SCIENCES'),
('GENERAL SOCIAL SCIENCES', 'GENERAL SOCIAL SCIENCES'),
('ECONOMICS', 'ECONOMICS'),
('CRIMINOLOGY', 'CRIMINOLOGY'),
('GEOGRAPHY', 'GEOGRAPHY'),
('INTERNATIONAL RELATIONS', 'INTERNATIONAL RELATIONS'),
('POLITICAL SCIENCE AND GOVERNMENT', 'POLITICAL SCIENCE AND GOVERNMENT'),
('SOCIOLOGY', 'SOCIOLOGY'),
('MISCELLANEOUS SOCIAL SCIENCES', 'MISCELLANEOUS SOCIAL SCIENCES')], validators=[InputRequired()], render_kw={"placeholder": "Major"})

    nation = SelectField(choices=[('Afghan', 'Afghan'),
('Albanian', 'Albanian'),
('Algerian', 'Algerian'),
('American', 'American'),
('Andorran', 'Andorran'),
('Angolan', 'Angolan'),
('Antiguans', 'Antiguans'),
('Argentinean', 'Argentinean'),
('Armenian', 'Armenian'),
('Australian', 'Australian'),
('Austrian', 'Austrian'),
('Azerbaijani', 'Azerbaijani'),
('Bahamian', 'Bahamian'),
('Bahraini', 'Bahraini'),
('Bangladeshi', 'Bangladeshi'),
('Barbadian', 'Barbadian'),
('Barbudans', 'Barbudans'),
('Batswana', 'Batswana'),
('Belarusian', 'Belarusian'),
('Belgian', 'Belgian'),
('Belizean', 'Belizean'),
('Beninese', 'Beninese'),
('Bhutanese', 'Bhutanese'),
('Bolivian', 'Bolivian'),
('Bosnian', 'Bosnian'),
('Brazilian', 'Brazilian'),
('British', 'British'),
('Bruneian', 'Bruneian'),
('Bulgarian', 'Bulgarian'),
('Burkinabe', 'Burkinabe'),
('Burmese', 'Burmese'),
('Burundian', 'Burundian'),
('Cambodian', 'Cambodian'),
('Cameroonian', 'Cameroonian'),
('Canadian', 'Canadian'),
('Cape Verdean', 'Cape Verdean'),
('Central African', 'Central African'),
('Chadian', 'Chadian'),
('Chilean', 'Chilean'),
('Chinese', 'Chinese'),
('Colombian', 'Colombian'),
('Comoran', 'Comoran'),
('Congolese', 'Congolese'),
('Costa Rican', 'Costa Rican'),
('Croatian', 'Croatian'),
('Cuban', 'Cuban'),
('Cypriot', 'Cypriot'),
('Czech', 'Czech'),
('Danish', 'Danish'),
('Djibouti', 'Djibouti'),
('Dominican', 'Dominican'),
('Dutch', 'Dutch'),
('East Timorese', 'East Timorese'),
('Ecuadorean', 'Ecuadorean'),
('Egyptian', 'Egyptian'),
('Emirian', 'Emirian'),
('Equatorial Guinean', 'Equatorial Guinean'),
('Eritrean', 'Eritrean'),
('Estonian', 'Estonian'),
('Ethiopian', 'Ethiopian'),
('Fijian', 'Fijian'),
('Filipino', 'Filipino'),
('Finnish', 'Finnish'),
('French', 'French'),
('Gabonese', 'Gabonese'),
('Gambian', 'Gambian'),
('Georgian', 'Georgian'),
('German', 'German'),
('Ghanaian', 'Ghanaian'),
('Greek', 'Greek'),
('Grenadian', 'Grenadian'),
('Guatemalan', 'Guatemalan'),
('Guinea-Bissauan', 'Guinea-Bissauan'),
('Guinean', 'Guinean'),
('Guyanese', 'Guyanese'),
('Haitian', 'Haitian'),
('Herzegovinian', 'Herzegovinian'),
('Honduran', 'Honduran'),
('Hungarian', 'Hungarian'),
('I-Kiribati', 'I-Kiribati'),
('Icelander', 'Icelander'),
('Indian', 'Indian'),
('Indonesian', 'Indonesian'),
('Iranian', 'Iranian'),
('Iraqi', 'Iraqi'),
('Irish', 'Irish'),
('Israeli', 'Israeli'),
('Italian', 'Italian'),
('Ivorian', 'Ivorian'),
('Jamaican', 'Jamaican'),
('Japanese', 'Japanese'),
('Jordanian', 'Jordanian'),
('Kazakhstani', 'Kazakhstani'),
('Kenyan', 'Kenyan'),
('Kittian and Nevisian', 'Kittian and Nevisian'),
('Kuwaiti', 'Kuwaiti'),
('Kyrgyz', 'Kyrgyz'),
('Laotian', 'Laotian'),
('Latvian', 'Latvian'),
('Lebanese', 'Lebanese'),
('Liberian', 'Liberian'),
('Libyan', 'Libyan'),
('Liechtensteiner', 'Liechtensteiner'),
('Lithuanian', 'Lithuanian'),
('Luxembourger', 'Luxembourger'),
('Macedonian', 'Macedonian'),
('Malagasy', 'Malagasy'),
('Malawian', 'Malawian'),
('Malaysian', 'Malaysian'),
('Maldivan', 'Maldivan'),
('Malian', 'Malian'),
('Maltese', 'Maltese'),
('Marshallese', 'Marshallese'),
('Mauritanian', 'Mauritanian'),
('Mauritian', 'Mauritian'),
('Mexican', 'Mexican'),
('Micronesian', 'Micronesian'),
('Moldovan', 'Moldovan'),
('Monacan', 'Monacan'),
('Mongolian', 'Mongolian'),
('Moroccan', 'Moroccan'),
('Mosotho', 'Mosotho'),
('Motswana', 'Motswana'),
('Mozambican', 'Mozambican'),
('Namibian', 'Namibian'),
('Nauruan', 'Nauruan'),
('Nepalese', 'Nepalese'),
('New Zealander', 'New Zealander'),
('Nicaraguan', 'Nicaraguan'),
('Nigerian', 'Nigerian'),
('Nigerien', 'Nigerien'),
('North Korean', 'North Korean'),
('Northern Irish', 'Northern Irish'),
('Norwegian', 'Norwegian'),
('Omani', 'Omani'),
('Pakistani', 'Pakistani'),
('Palauan', 'Palauan'),
('Panamanian', 'Panamanian'),
('Papua New Guinean', 'Papua New Guinean'),
('Paraguayan', 'Paraguayan'),
('Peruvian', 'Peruvian'),
('Polish', 'Polish'),
('Portuguese', 'Portuguese'),
('Qatari', 'Qatari'),
('Romanian', 'Romanian'),
('Russian', 'Russian'),
('Rwandan', 'Rwandan'),
('Saint Lucian', 'Saint Lucian'),
('Salvadoran', 'Salvadoran'),
('Samoan', 'Samoan'),
('San Marinese', 'San Marinese'),
('Sao Tomean', 'Sao Tomean'),
('Saudi', 'Saudi'),
('Scottish', 'Scottish'),
('Senegalese', 'Senegalese'),
('Serbian', 'Serbian'),
('Seychellois', 'Seychellois'),
('Sierra Leonean', 'Sierra Leonean'),
('Singaporean', 'Singaporean'),
('Slovakian', 'Slovakian'),
('Slovenian', 'Slovenian'),
('Solomon Islander', 'Solomon Islander'),
('Somali', 'Somali'),
('South African', 'South African'),
('South Korean', 'South Korean'),
('Spanish', 'Spanish'),
('Sri Lankan', 'Sri Lankan'),
('Sudanese', 'Sudanese'),
('Surinamer', 'Surinamer'),
('Swazi', 'Swazi'),
('Swedish', 'Swedish'),
('Swiss', 'Swiss'),
('Syrian', 'Syrian'),
('Taiwanese', 'Taiwanese'),
('Tajik', 'Tajik'),
('Tanzanian', 'Tanzanian'),
('Thai', 'Thai'),
('Togolese', 'Togolese'),
('Tongan', 'Tongan'),
('Trinidadian or Tobagonian', 'Trinidadian or Tobagonian'),
('Tunisian', 'Tunisian'),
('Turkish', 'Turkish'),
('Tuvaluan', 'Tuvaluan'),
('Ugandan', 'Ugandan'),
('Ukrainian', 'Ukrainian'),
('Uruguayan', 'Uruguayan'),
('Uzbekistani', 'Uzbekistani'),
('Venezuelan', 'Venezuelan'),
('Vietnamese', 'Vietnamese'),
('Welsh', 'Welsh'),
('Yemenite', 'Yemenite'),
('Zambian', 'Zambian'),
('Zimbabwean', 'Zimbabwean'),], validators=[InputRequired()], render_kw={"placeholder": "Nationality"})

    description = TextAreaField(validators=[
                                InputRequired(), Length(min=10, max=500)], render_kw={"placeholder": "Description. Consider adding contact information. Max of 500 characters."})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    confirm_password = PasswordField(validators=[
                                     InputRequired(), EqualTo('password', message='Passwords must match')], render_kw={"placeholder": "Confirm Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = Users.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE city = '{current_user.city}' AND username <> '{current_user.username}' AND (major = '{current_user.major}' OR nation = '{current_user.nation}')")
    rows = cursor.fetchall()

    print(rows)

    return render_template('dashboard.html', rows=rows, user=current_user)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = Users(username=form.username.data, password=hashed_password, city=form.city.data, major=form.major.data, nation=form.nation.data, description=form.description.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)

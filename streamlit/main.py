import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Configuration avancée de la page
st.set_page_config(
    page_title="Yelp Data Analysis",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé pour améliorer le design
st.markdown("""
<style>
    /* Style principal */
    .main-header {
        font-size: 3rem;
        color: #1f4e79;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 700;
        background: linear-gradient(90deg, #1f4e79, #ff6b6b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    /* Cartes métriques personnalisées */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        color: white;
        margin: 1rem 0;
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: bold;
        margin: 0.5rem 0;
    }
    
    .metric-label {
        font-size: 1.1rem;
        opacity: 0.9;
    }
    
    /* Section headers */
    .section-header {
        color: #1f4e79;
        border-left: 4px solid #ff6b6b;
        padding-left: 1rem;
        margin: 2rem 0 1rem 0;
        font-weight: 600;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Navigation cards */
    .nav-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Info boxes */
    .info-box {
        background: linear-gradient(135deg, #74b9ff, #0984e3);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    /* Success box */
    .success-box {
        background: linear-gradient(135deg, #00b894, #00a085);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    /* Warning box */
    .warning-box {
        background: linear-gradient(135deg, #fdcb6e, #e17055);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    /* Dataframe styling */
    .dataframe {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
    }
    
    /* Hide streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Animation */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .fade-in {
        animation: fadeIn 0.8s ease-out;
    }
</style>
""", unsafe_allow_html=True)

image_path = "assets/images/"

# Sidebar avec design amélioré
with st.sidebar:
    st.markdown("""
    <div style='text-align: center; padding: 1rem; color: white;'>
        <h1>Navigation</h1>
        <p style='opacity: 0.8;'>Explorez les données Yelp</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation avec icônes
    sections = {
        "Accueil": "Accueil",
        "Vue d'ensemble": "Vue d'ensemble", 
        "Analyse des utilisateurs": "Analyse des utilisateurs",
        "Analyse des commerces": "Analyse des commerces",
        "Analyse des avis": "Analyse des avis",
        "Corrélations": "Corrélations",
        "Carte interactive": "Carte interactive"
    }
    
    selected_display = st.radio("", list(sections.keys()), label_visibility="collapsed")
    section = sections[selected_display]

# Page d'accueil
if section == "Accueil":
    st.markdown('<h1 class="main-header fade-in">Dashboard d\'Analyse Yelp</h1>', unsafe_allow_html=True)
    
    # Hero section
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="info-box fade-in">
            <h2 style='text-align: center; margin-top: 0;'>Bienvenue</h2>
            <p style='text-align: center; font-size: 1.1rem; line-height: 1.6;'>
                Explorez le dataset <strong>Yelp Academic</strong> avec des analyses avancées 
                et des visualisations interactives alimentées par <strong>Apache Spark</strong>.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Fonctionnalités en cards
    st.markdown('<h2 class="section-header">Fonctionnalités Principales</h2>', unsafe_allow_html=True)
    
    features_col1, features_col2 = st.columns(2)
    
    with features_col1:
        st.markdown("""
        <div class="success-box">
            <h3>Analyses Avancées</h3>
            <ul style='margin: 0; padding-left: 1.5rem;'>
                <li>Analyse de l'activité des utilisateurs</li>
                <li>Segmentation des commerces</li>
                <li>Scores d'influence et d'activité</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with features_col2:
        st.markdown("""
        <div class="warning-box">
            <h3>Visualisations</h3>
            <ul style='margin: 0; padding-left: 1.5rem;'>
                <li>Graphiques interactifs</li>
                <li>Cartes géographiques</li>
                <li>Tableaux de bord dynamiques</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # CTA
    st.markdown("""
    <div style='text-align: center; margin: 3rem 0;'>
        <p style='font-size: 1.2rem; color: #666;'>Commencez votre exploration dès maintenant !</p>
    </div>
    """, unsafe_allow_html=True)

# Vue d'ensemble avec métriques améliorées
elif section == "Vue d'ensemble":
    st.markdown('<h1 class="main-header">Statistiques Générales</h1>', unsafe_allow_html=True)
    
    # Métriques principales avec design personnalisé
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Utilisateurs</div>
            <div class="metric-value">1.99M</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Commerces</div>
            <div class="metric-value">150K</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Avis</div>
            <div class="metric-value">6.99M</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<h2 class="section-header">Modélisation des Données</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image(image_path + "schema.png", caption="Architecture du dataset Yelp")
    with col2:
        st.markdown("""
        <div class="info-box">
            <h4>Structure</h4>
            <p>Le dataset est organisé en 4 tables principales interconnectées pour optimiser les requêtes et analyses.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<h2 class="section-header">Traitement des Données</h2>', unsafe_allow_html=True)
    
    # Section de nettoyage avec accordéon
    with st.expander("Détails du nettoyage des données", expanded=False):
        st.markdown("""
        **Phase critique** de préparation garantissant la qualité des analyses :
        
        **Commerces (Business)** :
        - Suppression des entrées sans catégories, coordonnées, nom, note ou avis
        - Transformation des colonnes complexes (catégories, attributs)
        
        **Utilisateurs (User)** :
        - Nettoyage des données "elite"
        - Calcul des métriques d'engagement (ancienneté, amis, etc.)
        
        **Avis & Conseils** :
        - Suppression des contenus vides
        - Normalisation des dates
        """)
    
    # Images avec layout amélioré
    img_col1, img_col2 = st.columns(2)
    with img_col1:
        st.image(image_path + "prepocessing.png", caption="Suppression des valeurs nulles")
    with img_col2:
        st.markdown("""
        <div class="success-box">
            <h4>Résultats</h4>
            <p>Données nettoyées et optimisées pour des analyses fiables et performantes.</p>
        </div>
        """, unsafe_allow_html=True)

# Analyse des utilisateurs avec meilleur layout
elif section == "Analyse des utilisateurs":
    st.markdown('<h1 class="main-header">Analyse des Utilisateurs</h1>', unsafe_allow_html=True)
    
    # Tabs pour organiser le contenu
    tab1, tab2, tab3, tab4 = st.tabs(["Top Actifs", "Influenceurs", "Score d'Activité", "Fiabilité"])
    
    with tab1:
        st.markdown('<h3 class="section-header">Utilisateurs les plus actifs</h3>', unsafe_allow_html=True)
        st.image(image_path + "top_user_actif.png", caption="Top 10 - Nombre d'avis publiés")
    
    with tab2:
        st.markdown('<h3 class="section-header">Utilisateurs influents</h3>', unsafe_allow_html=True)
        st.image(image_path + "top_user_influent.png", caption="Top 10 - Nombre de followers")
    
    with tab3:
        st.markdown('<h3 class="section-header">Score d\'activité global</h3>', unsafe_allow_html=True)
        st.info("Métrique combinée : avis + tips + check-ins")
        st.image(image_path + "top_user_actif_score_activities.png", caption="Utilisateurs les plus engagés")
    
    with tab4:
        st.markdown('<h3 class="section-header">Utilisateurs les plus fiables</h3>', unsafe_allow_html=True)
        st.info("Comparaison des avis individuels avec la moyenne des commerces")
        
        resultat_df = pd.DataFrame({
            'Nom': ['Vicki', 'RuthMarie', 'Virginia', 'Namir', 'Vi', 'Mary', 'Robert', 'Benjamin', 'Bob', 'Blake'],
            'Score de Fiabilité': [0.9999, 0.9998, 0.9992, 0.9991, 0.9991, 0.9988, 0.9987, 0.9986, 0.9986, 0.9985]
        })
        
        st.dataframe(resultat_df, use_container_width=True, hide_index=True)
        st.image(image_path + "top_user_reliable.png", caption="Classement par fiabilité")

# Analyse des commerces
elif section == "Analyse des commerces":
    st.markdown('<h1 class="main-header">Analyse des Commerces</h1>', unsafe_allow_html=True)
    
    # Sections avec séparateurs visuels
    st.markdown('<h2 class="section-header">Analyse Géographique</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Villes les plus actives")
        st.image(image_path + "top_villes_with_entreprise.png", caption="Nombre de commerces par ville")
    
    with col2:
        st.markdown("### Villes les mieux notées")
        st.image(image_path + "top_city_mean.png", caption="Note moyenne par ville (min. 100 commerces)")
    
    st.markdown('<h2 class="section-header">Analyse par Catégorie</h2>', unsafe_allow_html=True)
    
    st.markdown("### Catégories populaires")
    st.image(image_path + "top_categories.png", caption="Top 15 des catégories")
    
    st.markdown("### Catégories les mieux notées")
    
    # Données avec styling amélioré
    resultat_top_commerces = pd.DataFrame({
        'Catégorie': ['Reiki', 'Barre Classes', 'DJs', 'Personal Chefs', 'Team Building Activities', 
                     'Paint & Sip', 'Life Coach', 'Event Photography', 'Pilates', 'Traditional Chinese Medicine'],
        'Note Moyenne': [4.68, 4.61, 4.57, 4.56, 4.56, 4.55, 4.54, 4.53, 4.53, 4.52],
        'Nb. Commerces': [201, 158, 127, 116, 136, 109, 130, 325, 294, 174]
    })
    
    # Graphique avec Plotly pour plus d'interactivité
    fig = px.bar(
        resultat_top_commerces, 
        x='Note Moyenne', 
        y='Catégorie',
        orientation='h',
        title='Top 10 des catégories par note moyenne',
        color='Note Moyenne',
        color_continuous_scale='viridis',
        text='Note Moyenne'
    )
    fig.update_layout(height=500, showlegend=False)
    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    st.plotly_chart(fig, use_container_width=True)
    
    st.dataframe(resultat_top_commerces, use_container_width=True, hide_index=True)

# Analyse des avis
elif section == "Analyse des avis":
    st.markdown('<h1 class="main-header">Analyse des Avis</h1>', unsafe_allow_html=True)
    
    # Métriques d'avis
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Évolution temporelle")
        st.image(image_path + "avis_evolution.png", caption="Croissance des avis par année")
    
    with col2:
        st.markdown("### Longueur des avis")
        st.image(image_path + "avis_length_distribution.png", caption="Distribution de la longueur")
        
    st.markdown("### Top 3 catégories avec le plus grand nombre d'avis chaque année")    
    st.image(image_path + "top_categories_year.png", caption="Tendance des catégories par année")
        
    

# Corrélations avec analyse approfondie
elif section == "Corrélations":
    st.markdown('<h1 class="main-header">Analyses de Corrélation</h1>', unsafe_allow_html=True)
    
    # Métriques de corrélation
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-box">
            <h3>Note vs Nombre d'avis</h3>
            <p style='font-size: 1.5rem; font-weight: bold; text-align: center;'>
                Corrélation: 0.0596
            </p>
            <p style='text-align: center;'>Corrélation faible positive</p>
        </div>
        """, unsafe_allow_html=True)
        st.image(image_path + "correlation_note_moyenne_nombre_avis.png")
    
    with col2:
        st.markdown("""
        <div class="success-box">
            <h3>Prix vs Note</h3>
            <p style='font-size: 1.5rem; font-weight: bold; text-align: center;'>
                Corrélation: 0.0720
            </p>
            <p style='text-align: center;'>Légère tendance positive</p>
        </div>
        """, unsafe_allow_html=True)
        st.image(image_path + "distribution_price_note.png")

# Carte interactive
elif section == "Carte interactive":
    st.markdown('<h1 class="main-header">Visualisation Géographique</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="warning-box">
        <h3>Section en développement</h3>
        <p>La carte interactive sera bientôt disponible avec :</p>
        <ul>
            <li>Localisation des commerces</li>
            <li>Filtrage par catégorie et note</li>
            <li>Recherche géographique avancée</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Placeholder pour la carte future
    st.info("Utilisez les filtres ci-dessous pour personnaliser l'affichage de la carte")
    
    filter_col1, filter_col2, filter_col3 = st.columns(3)
    with filter_col1:
        st.selectbox("Catégorie", ["Toutes", "Restaurants", "Services", "Shopping"])
    with filter_col2:
        st.slider("Note minimum", 1.0, 5.0, 3.0)
    with filter_col3:
        st.multiselect("Villes", ["Las Vegas", "Phoenix", "Toronto", "Charlotte"])

# Footer
st.markdown("""
<div style='text-align: center; padding: 2rem; color: #666; border-top: 1px solid #eee; margin-top: 3rem;'>
    <p>Dashboard Yelp Analytics • Powered by Streamlit & Apache Spark</p>
</div>
""", unsafe_allow_html=True)
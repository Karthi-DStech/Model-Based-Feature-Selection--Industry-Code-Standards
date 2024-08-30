def call_feature_engineering(feature_engg_name, *args, **kwargs):
    
    if feature_engg_name.lower() == "calculate_total_days":
        from feature_engineering.feature_engineering_combo import FeatureEngineeringLogics

        feature_engg = FeatureEngineeringLogics(*args, **kwargs)
        feature_engg_func = feature_engg.calculate_total_days
        return feature_engg_func
    
    elif feature_engg_name.lower() == "separate_date_columns":
        from feature_engineering.feature_engineering_combo import FeatureEngineeringLogics

        feature_engg = FeatureEngineeringLogics(*args, **kwargs)
        feature_engg_func = feature_engg.separate_date_columns
        return feature_engg_func
    
    else:
        raise ValueError("Feature Engineering method not found. Please check the method name.")
    
    
# ---- OTHER METHODS WILL BE ADDED HERE ----
    
    

        
   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
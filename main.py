import fastf1
import os

# Enable the cache
def enable_cache():
    cache_dir = ".fastf1-cache"

    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)

    fastf1.Cache.enable_cache(cache_dir)
    print(f"Fastf1 cache enabled \nenabled at: {cache_dir}")

def load_session(year, round_number, session_type):
    session = fastf1.get_session(year , round_number , session_type)
    session.load()
    return session




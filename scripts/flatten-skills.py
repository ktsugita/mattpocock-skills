import os
import shutil

def main():
    skills_dir = "skills"
    if os.path.exists(skills_dir):
        categories = [
            d for d in os.listdir(skills_dir)
            if os.path.isdir(os.path.join(skills_dir, d))
        ]
        for cat in categories:
            cat_path = os.path.join(skills_dir, cat)
            for item in os.listdir(cat_path):
                src = os.path.join(cat_path, item)
                dst = os.path.join(skills_dir, item)
                if os.path.isdir(src):
                    shutil.move(src, dst)
            shutil.rmtree(cat_path)

    if os.path.exists(".claude-plugin/plugin.json"):
        shutil.copy(".claude-plugin/plugin.json", "plugin.json")

    if os.path.exists("README.md"):
        with open("README.md", "r", encoding="utf-8") as f:
            readme_content = f.read()

        banner = """# Matt Pocock Skills (Antigravity CLI Edition)

> [!NOTE]
> This branch is automatically flattened for Antigravity CLI (`agy`).
>
> ```bash
> agy plugin install https://github.com/ktsugita/mattpocock-skills/tree/agy mattpocock-skills
> ```

---

"""
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(banner + readme_content)

if __name__ == "__main__":
    main()

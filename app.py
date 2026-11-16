if st.button("Delete",key=f"del_{task['id']}"):
                delete_task(task["id"],user["id"])
                st.rerun()

# ----------------------------- ACCOUNT -----------------------------
elif page == "Account":
    st.markdown('<div class="hero"><div class="eyebrow">✦ IDENTITY & PREFERENCES</div><h1>Account</h1>'
                '<p>Manage your NEXORA profile and review workspace information.</p></div>',unsafe_allow_html=True)
    st.markdown("### Profile")
    st.write(f"**Username:** {user['username']}")
    st.write(f"**Email:** {user['email']}")
    st.write("**Account ID:** " + str(user["id"]))
    st.divider()
    st.markdown("### AI connection")
    if gemini_key():
        st.success("Gemini API key detected. Generative AI is enabled.")
    else:
        st.warning("Gemini API key not configured. NEXORA is using its built-in offline assistant.")
        st.markdown("To enable Gemini, add a secret named `GEMINI_API_KEY` in your Streamlit app settings.")
    st.markdown("### Privacy & storage")
    st.info("This prototype stores account and task records in a local SQLite database. Do not use it for sensitive information. On Community Cloud, local files are not guaranteed to persist across rebuilds or restarts. Use a managed database such as Supabase for production.")
    if st.button("Export my tasks"):
        task_df = pd.DataFrame(get_tasks(user["id"]))
        st.download_button("Download tasks CSV",task_df.to_csv(index=False).encode(),"nexora_tasks.csv","text/csv")

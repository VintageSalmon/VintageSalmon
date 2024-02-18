using UnityEngine.SceneManagement;
using UnityEngine;
using TMPro;

public class MainMenu : MonoBehaviour
{

    // Update is called once per frame
    public void PlayGame()
    {
        //Load the scene
        SceneManager.LoadScene("Game");
    }
}
